from telebot import TeleBot, types
from random import randint, choice, shuffle

def token(token):
	global bot
	bot = TeleBot(token)

def send(ID,text,options=None):
	if options==None:
		bot.send_message(ID, text, parse_mode="Markdown")
	else:
		markup = types.ReplyKeyboardMarkup()
		buttons = [types.KeyboardButton(x) for x in options]
		if len(buttons)<=3:
			markup.row(*buttons)
		elif len(buttons)<=8:
			markup.row(*buttons[:len(buttons)//2])
			markup.row(*buttons[len(buttons)//2:])
		bot.send_message(ID, text, reply_markup=markup, parse_mode="Markdown")

def send_pic(ID,file):
	with open(file,"rb") as pic:
		bot.send_photo(ID, pic)

def handle(func):
	@bot.message_handler(content_types=["text"])
	def new_func(message):
		return func(message.chat.id,message.chat.first_name,message.text)
	return new_func

def start():
	bot.polling(non_stop=True)
