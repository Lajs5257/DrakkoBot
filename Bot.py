import os
import qrcode
import pyshorteners
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ChatAction, InlineKeyboardMarkup, InlineKeyboardButton

INPUT_TEXT = 0
INPUT_URL = 0
INPUT_MUSICA = 0

#objetos
button1 = InlineKeyboardButton(
        text='Sobre mi',
        url='https://github.com/Lajs5257'
    )

button2 = InlineKeyboardButton(
        text='Repositorio del bot',
        url='https://github.com/Lajs5257/DrakkoBot'
    )

button3 = InlineKeyboardButton(
        text='Generar Codigo QR',
        callback_data='qr'
    )

button4 = InlineKeyboardButton(
        text='Buscar musica',
        callback_data='musica'
    )

button5 = InlineKeyboardButton(
        text='Acotartar enlace',
        callback_data='url'
    )


def input_text(update, context):
    try:
        text = update.message.text

        filename = generate_qr(text)

        chat = update.message.chat

        send_qr(filename,chat)

        return ConversationHandler.END
    except Exception as error:
        print("Error 001 {}".format(error.args[0]))


def input_url(update, context):
    try:
        chat = update.message.chat
        url = update.message.text
        #Acotar enlace

        s = pyshorteners.Shortener()
        short3 = s.chilpit.short(url)

        chat.send_action(
            action=ChatAction.TYPING,
            timeout=None
        )
        chat.send_message(
            text=short3
        )

        return ConversationHandler.END
    except Exception as error:
        print("Error 002 {}".format(error.args[0]))


def input_musica(update, context):
    try:
        chat = update.message.chat

        chat.send_action(
            action=ChatAction.TYPING,
            timeout=None
        )
        chat.send_message(
            text='hola banda'
        )

        return ConversationHandler.END
    except Exception as error:
        print("Error 003 {}".format(error.args[0]))


def generate_qr(text):
    try:
        filename = text + '.jpg'

        img = qrcode.make(text)
        img.save(filename)

        return filename
    except Exception as error:
        print("Error 004 {}".format(error.args[0]))


def send_qr(filename,chat):
    try:
        chat.send_action(
            action=ChatAction.UPLOAD_PHOTO,
            timeout=None
        )

        chat.send_photo(
            photo=open(filename, 'rb')
        )

        os.unlink(filename)
    except Exception as error:
        print("Error 005 {}".format(error.args[0]))


def start(update, context):
    try:
        chat = update.message.chat
        chat.send_action(
            action=ChatAction.TYPING,
            timeout=None
        )
        update.message.reply_text(text='Hola yo soy Drakko_bot, ¿que haremos?\n\n',reply_markup=InlineKeyboardMarkup([
          [button1],
            [button2],
            [button3],
            [button4],
            [button5]
        ]))
    except Exception as error:
        print("Error 006 {}".format(error.args[0]))


def help(update, context):
    try:
        chat = update.message.chat
        chat.send_action(
            action=ChatAction.TYPING,
            timeout=None
        )
        update.message.reply_text('¿Que ocupas?')
    except Exception as error:
        print("Error 007 {}".format(error.args[0]))


def qr_command_handler(update, context):
    try:
        update.message.reply_text('Envíame el texto para generarte un código QR')

        return INPUT_TEXT
    except Exception as error:
        print("Error 008 {}".format(error.args[0]))


def qr_callback_handler(update, context):
    try:
        query = update.callback_query
        query.answer()

        query.edit_message_text(
            text='Envíame el texto para generarte un código QR'
        )

        return INPUT_TEXT
    except Exception as error:
        print("Error 009 {}".format(error.args[0]))


def url_callback_handler(update, context):
    try:
        query = update.callback_query
        query.answer()

        query.edit_message_text(
            text='Envíame un enlace para acortarlo'
        )
        return INPUT_URL
    except Exception as error:
        print("Error 010 {}".format(error.args[0]))


def musica_callback_handler(update, context):
    try:
        query = update.callback_query
        #query()
        query.edit_message_text(
            text='Mira, si ocupas música este link será uno que te gustará, podras encontrar toda la musica que necesites, usalo como tu spotify, sin mencionar que las descargas son en una gran calidad\nhttps://t.me/DeezerMusicBot',reply_markup=InlineKeyboardMarkup([
            [button1],
            [button2],
            [button3],
            [button4],
            [button5]
        ]))
    except Exception as error:
        print("Error 011 {}".format(error.args[0]))


def musica(update,context):
    try:
        chat = update.message.chat
        chat.send_action(
           action=ChatAction.TYPING,
           timeout=None
        )
        update.message.reply_text('Mira, si ocupas música este link será uno que te gustará, podras encontrar toda la musica que necesites, usalo como tu spotify, sin mencionar que las descargas son en una gran calidad\nhttps://t.me/DeezerMusicBot')
    except Exception as error:
        print("Error 012 {}".format(error.args[0]))


if __name__ == '__main__':
    try:
        updater = Updater(token='1885973491:AAHcTHNllolMMfsslMrMbfROzVkWoYer4Rg',use_context=True)

        dp = updater.dispatcher

        dp.add_handler(CommandHandler('start',start))
        dp.add_handler(CommandHandler('musica', musica))
        dp.add_handler(CommandHandler('help', help))

        dp.add_handler(ConversationHandler(
            entry_points=[
                CommandHandler('qr', qr_command_handler),
                CallbackQueryHandler(pattern='qr', callback=qr_callback_handler),
                CallbackQueryHandler(pattern='musica', callback=musica_callback_handler),
                CallbackQueryHandler(pattern='url', callback=url_callback_handler)
            ],
            states={
                INPUT_URL: [MessageHandler(Filters.text, input_url)],
                INPUT_MUSICA: [MessageHandler(Filters.text, input_musica)],
                INPUT_TEXT: [MessageHandler(Filters.text, input_text)]
            },
            fallbacks=[]
        ))

        updater.start_polling()
        print('Bot corriendo')
        updater.idle()
    except Exception as error:
        print("Error main {}".format(error.args[0]))
