
from turtle import update
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import configparser
import json
import random
import datetime

class Bot:
    HELP_MSG = "Available commands:\n" \
               "    /help -- List all the commends\n" \
               "    /workoutPlan -- Check your own gym plan\n" \
               "    /groups -- Gym by selecting major muscle groups in your body\n" \
               "    /tips -- Getting some random gym tips everyday!\n" \

    DESP = "Hello, I'm GymWithMeBot. This is a gym manegment chatbot that delivers fitness workouts.\n"\
               "    See what I can do -> '/help'\n" \

    def __init__(self) -> None:
        # read config file for testing
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.updater = Updater(
            token=(self.config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
        # # Set up logger and dispatcher
        self.logger = logging.getLogger(__name__) # Create logger
        self.dp = self.updater.dispatcher
        
        
    # You can set this logging module, so you will know when and why things do not work as expected
        self.info = logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    

    def start(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /help is issued."""
        self.logger.info("/start call")
        update.message.reply_text(self.DESP)

    def any_text(self, update: Update, context: CallbackContext) -> None:
        """Bot response on not coded text"""
        self.logger.info(f"unknown command called ({update.message.text})")
        update.message.reply_text(f"Unknown command: {update.message.text} -> /help")

    def help_command(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /help is issued."""
        self.logger.info("/help call")
        update.message.reply_text(self.HELP_MSG)
    
    def groups(self, update: Update, context: CallbackContext) -> None:
        self.keyboard = [[InlineKeyboardButton("chest", callback_data='1'),
                 InlineKeyboardButton("Back", callback_data='2'),
                 InlineKeyboardButton("abdominals", callback_data='3'),
                 InlineKeyboardButton("legs", callback_data='4'),
                 InlineKeyboardButton("arms", callback_data='5'),
                 InlineKeyboardButton("shoulders", callback_data='6')],
                [InlineKeyboardButton("Assign me please", callback_data='7')]]

        self.reply_markup = InlineKeyboardMarkup(self.keyboard)

        update.message.reply_text('Please choose:', reply_markup=self.reply_markup)

    def training(self,context:workout, workout_msg):
     """
     Builds the workout for the day.
     :return: A workout dictionary with the workout details and a string representation of the workout.
     """
    with open("exercise.json", "r") as f:
        exercises = json.load(f)
        f.close()
    workout = {k: random.choice(v) for k, v in exercises.items()}
    msg_intro = "Here is today's workout: \n"
    exercise_msg = "\n".join([k + ": " + v for k, v in workout.items()])
    workout_msg = "\n".join([msg_intro, exercise_msg])
    self.logger.info("/.workout")
    update.message.reply_text(self.workout_msg)


        
    