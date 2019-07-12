import logging
from datetime import datetime
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

import os
os.chdir('C:\\Users\\212587697\\Codigos\\MokitaBot')

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,  text='Escolha /atividades ou /debrifar')

def debrifar(bot, update):
    bot.send_message(chat_id=update.message.chat_id,  text='debrief')

def atividades(bot, update):
    bot.send_message(chat_id=update.message.chat_id,  text='atividades')
    # custom_keyboard = [['Debrifar', 'Ver DPOD'],  ['Configurações']]
    # reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    # _mensagem = "Bem vindo ao MokitaBot! Debrief fácil e rápido, na palma da mão"
    # update.message.reply_text("Please choose from the following : ", reply_markup=reply_markup)

def recover_user_feedback(bot, update):

    if (update.message.text == 'debrief'):
        _mensagem = "Selecione um laborcode abaixo:"
        custom_keyboard = [['Labor', 'Troubleshoot', 'Travel'], ['Finalizar']]
        bot.send_message(chat_id=update.message.chat_id,  text=_mensagem,  reply_markup=ReplyKeyboardMarkup(custom_keyboard))

    if (update.message.text == 'atividades'):
        _mensagem = "Atividades de hoje:"
        custom_keyboard = [['UDV4-06', 'UDV3-05', 'UDV2-07']]
        bot.send_message(chat_id=update.message.chat_id,  text=_mensagem,  reply_markup=ReplyKeyboardMarkup(custom_keyboard))

    # if (update.message.text == 'Outros ->'):
    #     custom_keyboard = [['Inicio Weather', 'Fim Weather'],  ['Debrifar Parts'], ['Finalizar debrief']]
    #     _mensagem = "Selecione um laborcode abaixo:"
    #     bot.send_message(chat_id=update.message.chat_id, text=_mensagem, reply_markup=ReplyKeyboardMarkup(custom_keyboard))

# def caps(bot, update, args):
#     text_caps = ' '.join(args).upper()
#     bot.send_message(chat_id=update.message.chat_id, text=text_caps)
# dispatcher.add_handler(CommandHandler('caps', caps, pass_args=True))

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    token = '816169093:AAGaEPFBcQyPe6_lh4XuMPtU7F8Bf57tkE8'
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('debrifar', debrifar))
    dispatcher.add_handler(CommandHandler('atividades', atividades))
    # dispatcher.add_handler(CallbackQueryHandler(debrief_menu, pattern='Debrifar'))
    dispatcher.add_handler(MessageHandler(Filters.text, recover_user_feedback))

    updater.start_polling()

    updater.idle()




    # chat_id = bot.get_updates()[-1].message.chat_id
