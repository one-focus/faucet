import sys
import telebot
import requests

address = sys.argv[1]
response = requests.get(url=f'https://faucet.ropsten.be/donate/{address}').json()
bot = telebot.TeleBot("1275523107:AAF_5t_r80J55Pl-JcVeLcVVOsl7kadqAc4")
if 'msg' in response and 'msg' != 'queue is full':
    bot.send_message(chat_id=-407923666, text=f'🟢 {response["msg"]}')
