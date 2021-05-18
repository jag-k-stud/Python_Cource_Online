from weather import get_weather
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def weather(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(get_weather())


def new_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello,')


updater = Updater('1854532819:AAHzcrGBi250fRxiCgC4lwsa0LOrWWBVy0o', use_context=True)

updater.dispatcher.add_handler(CommandHandler('weather', weather))
updater.dispatcher.add_handler(CommandHandler('hello', new_command))

updater.start_polling()
updater.idle()
