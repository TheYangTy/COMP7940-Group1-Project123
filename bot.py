from telegram import *
from telegram.ext import *
import logging
import configparser
import random
import responses
# A simple python wrapper for the Firebase API. pip install pyrebase
import pyrebase



# For use with only user based authentication we can create the following configuration:
config = {
  "apiKey": "AIzaSyCAXP4sN3HmsYmRUGRKByMl-nn6XGnSZu4",
  "authDomain": "depolyingtelegrambot.firebaseapp.com",
  "databaseURL": "https://depolyingtelegrambot-default-rtdb.firebaseio.com",
  "storageBucket": "depolyingtelegrambot.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

class Bot:
    # help message and GymWithMeBot Introduction
    HELP_MSG = "Available commands:\n" \
               "    /start -- GymWithMeBot Introduction\n" \
               "    /list -- List all the commends\n" \
               "    /groups -- Gym by selecting major muscle groups in your body\n" \
               "    /source_code -- Acessed source code\n" \

    DESP = "Hello, I'm GymWithMeBot. This is a gym manegment chatbot that delivers fitness workouts.\n"\
               "    See what I can do -> '/list'\n" \
    
    # init progress
    def __init__(self) -> None:
        # read config file for testing
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.updater = Updater(
            token=(self.config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
        # # Set up logger and dispatcher
        self.logger = logging.getLogger(__name__) # Create logger
        self.logger.setLevel(logging.INFO)
        self.dp = self.updater.dispatcher # name dispatcher

    # bot introduction
    def start(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /help is issued."""
        self.logger.info("/start call")
        update.message.reply_text(self.DESP)

    # reply to misunderstand message
    def any_text(self, update: Update, context: CallbackContext) -> None:
        """Bot response on not coded text"""
        self.logger.info(f"unknown command called ({update.message.text})")
        update.message.reply_text(f"Unknown command: {update.message.text} -> /help")

    # list all the commands
    def list(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /help is issued."""
        self.logger.info("/list call")
        update.message.reply_text(self.HELP_MSG)
    
    # get firebase back workout data
    def back(self, update: Update, context: CallbackContext) -> None:
            self.all_methods = db.child("methods").child("back").get()
            all_methods_length =len(self.all_methods.each())
            ranindex = random.randint(0,all_methods_length-1)
            method = self.all_methods.each()[ranindex]
            update.message.reply_text(method.val())
    
    # get firebase chest workout data
    def chest(self, update: Update, context: CallbackContext) -> None:
            self.all_methods = db.child("methods").child("chest").get()
            all_methods_length =len(self.all_methods.each())
            ranindex = random.randint(0,all_methods_length-1)
            method = self.all_methods.each()[ranindex]
            update.message.reply_text(method.val())

    # Get workout function by different areas
    def groups(self, update: Update, context: CallbackContext) -> None:
        self.logger.info("/groups call")
        update.message.reply_text("Please choose your target muscles area: /back /chest\n Other areas will be availiable soon")

    # Show source_code
    def source_code(self, update: Update, context):
        update.message.reply_text("the source code can be accessed here\n {Github}\n https://github.com/TheYangTy/COMP7940-Group1-Project123")


    # Bot response function
    def handle_message(self, update: Update, context):
        self.text = str(update.message.text).lower()
        logging.info(f'User ({update.message.chat.id}) says: {self.text}')
        self.response = responses.get_response(self.text)
        update.message.reply_text(self.response)

        

    

        
    