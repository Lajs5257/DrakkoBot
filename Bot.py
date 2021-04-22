from telegram.ext import  Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Hola")

if __name__ == '__main__':

    updater = Updater(token="TuToken",use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start))

    updater.start_polling()
    print("Bot corriendo")
    updater.idle()
