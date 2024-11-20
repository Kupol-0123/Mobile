from telebot import *
from random import *

API_TOKEN = '8001281886:AAGB1apo5WMuBr1VBDQYyESCGg-rOTHgf40'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}! Давай поиграем в игру. Тебе будет загадоно слово и ты должен будешь отгодать \nу тебя 6 попыток. ')
	bot.send_message(message.chat.id, 'Чтобы начать напишите команду /begin.')

@bot.message_handler(commands=['begin'])	
def wordly(message):
	global word, i
	bot.send_message(message.chat.id, 'Вы начили игру вордли. Вам загадоно одно слово, которое вам предстоит отгодать, у вас есть 6 попыток. ')
	i = 6
	words = ['Завод']
	word = choice(words)
	bot.send_message(message.chat.id, f'{word[0]}_ _ _ {word[4]}')
	bot.send_message(message.chat.id, 'Введите слово: ')
	bot.register_next_step_handler(message,startgame)
def startgame(message):
	input_word = message.text
	if len(input_word) > 5 or len(input_word) < 5:
		bot.send_message(message.chat.id, f'У вас меньше или больше букв, чем 5!')
		bot.register_next_step_handler(message,startgame)
	else:
		if input_word == word:
			bot.send_message(message.chat.id, f'Поздравляю! Вы угадли слово, \nзагадоное слово было: {word}. ')
		else:
			bot.send_message(message.chat.id, f'Нет не правильно попробуй еще раз. У тебя осталось {i} попыток!')
			bot.register_next_step_handler(message,startgame)
		if i == 0:
			bot.send_message(message.chat.id, f'Нет к сожалению у тебя не получилось.  \nзагадоное слово было: {word}.')		
				




if __name__ == '__main__':
    bot.polling(none_stop=True)
