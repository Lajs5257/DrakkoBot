from telegram.ext import  Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Hola")

if __name__ == '__main__':

    updater = Updater(token="530962145:AAHwsNM6c3rHD7Kl4fgAo7gqqF4I0CZ8W8E",use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start))

    updater.start_polling()
    print("Bot corriendo")
    updater.idle()
