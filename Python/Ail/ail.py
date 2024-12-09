from telebot import *
from time import *
from random import *

API_TOKEN = '8001281886:AAGB1apo5WMuBr1VBDQYyESCGg-rOTHgf40'
bot = telebot.TeleBot(API_TOKEN)

users = {}

rooms = {"💻 IT":'it',
		"🎸 Музыка":'music',
		"🎙 Актовый зал":'act',
		"🍕 Столовая":'table',
		"📖 Учительская":'teachers_room',
		" Мед. пункт":'med_punckt',
		"Робототехника":'robot',
		"Арт":'art',
		"Начальные кл.":'little_class',
		"Директорская":'director',х
		"Лаборатория":'laborant',
		"Классы":'class',
		"Двор":'dvor',
		"Охрана":'security',
		"Спортивная зона":'sport_zone',
		"0 этаж":'0_th',
		"1 этаж":'1_st',
		"2 этаж":'2_nd',
		"Начало":'start'}

@bot.message_handler(commands=['start'])
def welcome(message):
	if not message.chat.id in users
		users[message.chat.id] = False
	bot.send_message(message.chat.id, f"Здраствуйте {message.chat.first_name}! Добро пожаловать в школу AIL. Что вы хотите бы узнать?")
	bot.send_message(message.chat.id, "/excursion - Проведем экскурсию по нашей школе! \n/wordly - игра в вордли \n/help - помощь")
	file = open('AIL_Start.png', 'rb')
	bot.send_photo(message.chat.id, file)


# @bot.message_handler(commands=['wordly'])
# def wordly(message):
#     global word,  unword, word_back, active, iol
#     words = "завод навоз сосна мячик замок актёр банан барин барка бисер благо бомба бурка валет варка вилка виски ворон груша думка".split()
#     word = choice(words).upper()
#     word = list(word)
#     word_back = "".join(word)
#     word_back = word_back.capitalize()
#     iol = -1
#     unword = ""
#     # bot.send_message(message.chat.id, "\n".join([" ".join(unword[i*5:i*5+5]) for i in range(5)]))
#     bot.send_message(message.chat.id, 'Введите слово: ')
#     active = True
#     bot.register_next_step_handler(message, start_game)

# def start_game(message):
#     global iol, active, unword
#     if active:
#         iol = iol + 1
#         input_word = message.text.upper()
#         if len(input_word) > 5 or len(input_word) < 5:
#             bot.send_message(message.chat.id, 'Ваше слово больше или меньше 5 букв!!')
#             bot.send_message(message.chat.id, 'Введите слово: ')
#             iol = iol - 1
#             bot.register_next_step_handler(message, start_game)
#         else:
#             input_word = list(input_word)
#             unword = unword + find(word, input_word)
#             bot.send_message(message.chat.id,"\n".join([" ".join(unword[i*5:i*5+5]) for i in range(len(unword)//5)]))
#             bot.send_message(message.chat.id, 'Введите слово: ')
#             bot.register_next_step_handler(message,start_game)  
#             if input_word == word:
#                 bot.send_message(message.chat.id,f"Поздравляем! Вы угадали слово, загоданое слово было: <b>{word_back}</b>", parse_mode="HTML")
#                 active = False
#             elif iol == 4:
#                 bot.send_message(message.chat.id,f"К сожелению вы не угадали слова, загоданое слово было: <b>{word_back}</b>", parse_mode="HTML")
#                 active = False

# def find(word, input_word):
#     for b in range(0,5):
#         r = ""
#         for b in range(0,5):
#             if input_word[b] == word[b]:
#                 r = r + input_word[b].upper()
#             elif input_word[b] in word:
#                 r = r + input_word[b].lower()
#             else:
#                 r = r + '_'
#         return r


# unword = "dfagdfvasdhfsgahjthhyaerh5yrhysf"
# print("\n".join([" ".join(unword[i*5:i*5+5]) for i in range(5)]))

@bot.message_handler(commands=['excursion'])
def excursion(message):
	bot.send_message(message.chat.id, 'Добро Пожаловать в нашу школу😎! Академия инновации и лидерства!')
	markup = types.InlineKeyboardMarkup()
	item1 = types.InlineKeyboardButton("Поэтапно", callback_data='step')
	item2 = types.InlineKeyboardButton("Выборочно", callback_data='choice')
	markup.row(item1,item2)
	bot.send_message(message.chat.id, 'Пожалуйста выбирите вариант экскурсии: ', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
	if callback.data == 'step':
		pass  

	elif callback.data == 'start':
		bot.send_message(callback.message.chat.id, 'Вы вренулись на начало. \nДавайте начнем: ')
		markup = types.InlineKeyboardMarkup(row_width=3)
		markup.add(*[types.InlineKeyboardButton(room, callback_data=rooms[room]) for room in rooms])
		bot.send_message(callback.message.chat.id, 'Пожалуйста выбирите кабинет: ', reply_markup=markup)
	elif callback.data == 'choice':
		bot.send_message(callback.message.chat.id, 'Вы выбрали экскурсию выборочно. \nДавайте начнем: ')
		markup = types.InlineKeyboardMarkup(row_width=3)
		markup.add(*[types.InlineKeyboardButton(room, callback_data=rooms[room]) for room in rooms])
		bot.send_message(callback.message.chat.id, 'Пожалуйста выбирите кабинет: ', reply_markup=markup)
	elif callback.data == 'it':
		markup = types.InlineKeyboardMarkup(row_width=3)
		local_rooms = {"Музыка","Актовый зал","Столовая","0 этаж"}
		markup.add(*[types.InlineKeyboardButton(room, callback_data=rooms[room]) for room in local_rooms])
		bot.send_message(callback.message.chat.id, 'Вы попали в кабинет информатики. \nРядом с ним находятся: ', reply_markup=markup)
	elif callback.data == 'music':
		markup = types.InlineKeyboardMarkup(row_width=3)
		local_rooms = {"IT","Актовый зал","Столовая","0 этаж"}
		markup.add(*[types.InlineKeyboardButton(room, callback_data=rooms[room]) for room in local_rooms])
		bot.send_message(callback.message.chat.id, 'Вы попали в кабинет музыки. \nРядом с ним находятся: ', reply_markup=markup)
	elif callback.data == 'act':
		markup = types.InlineKeyboardMarkup(row_width=3)
		local_rooms = {"IT","Музыка","Столовая","0 этаж"}
		markup.add(*[types.InlineKeyboardButton(room, callback_data=rooms[room]) for room in local_rooms])
		bot.send_message(callback.message.chat.id, 'Вы попали в кабинет актогого зала. \nРядом с ним находятся: ', reply_markup=markup)
	elif callback.data == 'table':
		markup = types.InlineKeyboardMarkup(row_width=3)
		local_rooms = {"IT","Актовый зал","Музыка","0 этаж"}
		markup.add(*[types.InlineKeyboardButton(room, callback_data=rooms[room]) for room in local_rooms])
		bot.send_message(callback.message.chat.id, 'Вы попали в столовую. \nРядом с ним находятся: ', reply_markup=markup)
	elif callback.data == '0_th':
		markup = types.InlineKeyboardMarkup(row_width=3)
		local_rooms = {"IT","Актовый зал","Столовая","Музыка"}
		markup.add(*[types.InlineKeyboardButton(room, callback_data=rooms[room]) for room in local_rooms])
		bot.send_message(callback.message.chat.id, 'Вы попали на 0-ой этаж. \nНа 0-ом этаже есть кабинеты: ', reply_markup=markup)

	elif callback.data == '1_st':
		markup = types.InlineKeyboardMarkup(row_width=3)
		local_rooms = {"Учительская","Мед. пункт","Робототехника","Арт"}
		markup.add(*[types.InlineKeyboardButton(room, callback_data=rooms[room]) for room in local_rooms])
		bot.send_message(callback.message.chat.id, 'Вы попали на 1-ый этаж. \nна 1-ом этаже есть кабинеты: ', reply_markup=markup)




@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, "/excursion - Проведем экскурсию по нашей школе! \n/wordly - игра в вордли \n/help - помощь")




if __name__ == '__main__':
	bot.polling(none_stop=True)
