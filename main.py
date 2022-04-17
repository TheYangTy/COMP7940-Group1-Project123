from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from bot import Bot
import logging

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
logging.info('Starting Bot...')

def main():
    # logging information
    
    # Get class functions in bot.py
    bot = Bot()
    # on different commands - answer in Telegram
    bot.dp.add_handler(CommandHandler("start", bot.start))
    bot.dp.add_handler(CommandHandler("list", bot.list))
    bot.dp.add_handler(CommandHandler("groups", bot.groups))
    bot.dp.add_handler(CommandHandler('source_code',bot.source_code))
    # Any other message
    bot.dp.add_handler(MessageHandler(Filters.text, bot.handle_message))

    # Start idling for messages
    bot.updater.start_polling(1.0)
    # # Idle state give bot time to go in idle
    bot.updater.idle()
    


if __name__ == '__main__':
    main()
