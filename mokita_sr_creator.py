import logging
from datetime import datetime
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

import os
os.chdir('C:\\Users\\212587697\\Codigos\\MokitaBot')

def criar_sr(bot, update, args):
    lista_techs = ' '.join(args)
    print(args)
    bot.send_message(chat_id=update.message.chat_id,  text='Ok')

    custom_keyboard = [['UDV01', 'UDV02', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03', 'UDV03']]
    bot.send_message(chat_id=update.message.chat_id,  text='Qual turbina?',  reply_markup=ReplyKeyboardMarkup(custom_keyboard))

    bot.send_message(chat_id=update.message.chat_id,  text='Perfeito!',  reply_markup=ReplyKeyboardMarkup(custom_keyboard))

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    token = '873983820:AAEYjBHHjRC5yAr9vCYBdf2JRKtFb9w-Lf0'
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('criar_sr', criar_sr, pass_args=True))

    updater.start_polling()

    updater.idle()

    # chat_id = bot.get_updates()[-1].message.chat_id
