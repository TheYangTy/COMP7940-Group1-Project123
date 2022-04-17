
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext
import logging
import configparser
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
data = {
    "users/Morty/": {
        "name": "Mortimer 'Morty' Smith"
    },
    "users/Rick/": {
        "name": "Rick Sanchez"
    }
}

db.update(data)
user = db.child("users").get()
print(user.key()) # users

all_users = db.child("users").get()
for user in all_users.each():
    print(user.key()) # Morty
    print(user.val()) # {name": "Mortimer 'Morty' Smith"}








class Bot:
    HELP_MSG = "Available commands:\n" \
               "    /list -- List all the commends\n" \
               "    /workoutPlan -- Check your own gym plan\n" \
               "    /groups -- Gym by selecting major muscle groups in your body\n" \
               "    /source_code -- Acessed source code\n" \

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
        self.logger.setLevel(logging.INFO)
        self.dp = self.updater.dispatcher # name dispatcher

    def start(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /help is issued."""
        self.logger.info("/start call")
        update.message.reply_text(self.DESP)

    def any_text(self, update: Update, context: CallbackContext) -> None:
        """Bot response on not coded text"""
        self.logger.info(f"unknown command called ({update.message.text})")
        update.message.reply_text(f"Unknown command: {update.message.text} -> /help")

    def list(self, update: Update, context: CallbackContext) -> None:
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

    def source_code(self, update: Update, context):
        update.message.reply_text("the source code can be accessed here\n {Github}\n https://github.com/Rosonlau/COMP7940-Group1-Project")

    def handle_message(self, update: Update, context):
        self.text = str(update.message.text).lower()
        logging.info(f'User ({update.message.chat.id}) says: {self.text}')

    # Bot response
        self.response = responses.get_response(self.text)
        update.message.reply_text(self.response)


    

        
    