import os
import qrcode
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import ChatAction

INPUT_TEXT = 0


def input_text(update, context):

    text = update.message.text

    filename = generate_qr(text)

    chat = update.message.chat

    send_qr(filename, chat)

    return ConversationHandler.END


def generate_qr(text):
    filename = text + '.jpg'

    img = qrcode.make(text)
    img.save(filename)

    return filename


def send_qr(filename,chat):
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )

    chat.send_photo(
        photo=open(filename, 'rb')
    )

    os.unlink(filename)


def start(update, context):
    update.message.reply_text("Hola yo soy Drakko_bot, ¿que haremos?\n\n")


def help(update, context):
    update.message.reply_text("¿Que ocupas?")


def qr_command_handler(update, context):
    update.message.reply_text('Envíame el texto para generarte un código QR')

    return INPUT_TEXT


def musica(update, context):
    update.message.reply_text("Mira, si ocupas música este link será uno que te gustará, podras encontrar toda la musica que necesites, usalo como tu spotify, sin mencionar que las descargas son en una gran calidad\nhttps://t.me/DeezerMusicBot")


if __name__ == '__main__':

    updater = Updater(token="Token",use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('musica', musica))
    dp.add_handler(CommandHandler('help', help))

    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('qr',qr_command_handler)
        ],
        states={
            INPUT_TEXT: [MessageHandler(Filters.text, input_text)]
        },
        fallbacks=[]
    ))

    updater.start_polling()
    print("Bot corriendo")
    updater.idle()
