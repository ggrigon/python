
#!/usr/local/bin/python3

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Emoji, ForceReply, ReplyKeyboardMarkup, KeyboardButton
from telegram import ChatAction

import subprocess
import logging
import telegram


# Enable logging
logging.basicConfig(
        filename='/var/log/cartola.log',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Seja bem-vindo {0}'.format(update.message.from_user.first_name))
    bot.sendMessage(update.message.chat_id, text="Desenvolvedor do Bot @guilhermerigon")

#def hello(bot, update):
#    bot.sendMessage(update.message.chat_id,
#                    text='Hello {0}'.format(update.message.from_user.first_name))

def time(bot, update, args):
#    bot.sendMessage(update.message.chat_id, text="Aguarde um instante!")
    time = subprocess.check_output(['/home/silver/scripts/getjson.sh', ' '.join(args)])
    f = open("/tmp/saidacartolaphp.txt", encoding="utf-8")
#    bot.sendMessage(update.message.chat_id, text=f.read())
    bot.sendMessage(update.message.chat_id, text=f.read(), parse_mode=telegram.ParseMode.MARKDOWN)

def truqueiros(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
#    bot.sendMessage(update.message.chat_id, text="Aguarde um instante!")
    saida = subprocess.check_output(["/home/silver/scripts/cartola.py"])
#    output = saida.communicate()[0]
#    saida_message = output.decode("utf-8")
#    bot.sendMessage(update.message.chat_id, text=saida)
    bot.sendMessage(update.message.chat_id, text=saida.decode("utf-8"), parse_mode=telegram.ParseMode.MARKDOWN)


updater = Updater('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

updater.dispatcher.addHandler(CommandHandler('start', start))
updater.dispatcher.addHandler(CommandHandler('truqueiros', truqueiros))
updater.dispatcher.addHandler(CommandHandler('time', time, pass_args=True))

updater.start_polling()
updater.idle()
