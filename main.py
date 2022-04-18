# For testing

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from bot import Bot


def main():
    # Load your token and create an Updater for your Bot
    bot = Bot()
    # # register a dispatcher to handle message: here we register an echo dispatcher
    # echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    # dispatcher.add_handler(echo_handler)

    # on different commands - answer in Telegram
    bot.dp.add_handler(CommandHandler("help", bot.help_command))
    bot.dp.add_handler(CommandHandler("start", bot.start))
    bot.dp.add_handler(CommandHandler("groups", bot.groups))
    bot.dp.add_handler(CommandHandler("training",bot.exercise))
    # Any other message
    bot.dp.add_handler(MessageHandler(Filters.text, bot.any_text))
    
    # Start idling for messages
    bot.updater.start_polling()
    bot.updater.idle()
    bot.logger.info("Bot terminated.")


if __name__ == '__main__':
    main()
