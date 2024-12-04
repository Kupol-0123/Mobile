from telebot import *
from time import *
from random import *

API_TOKEN = '8001281886:AAGB1apo5WMuBr1VBDQYyESCGg-rOTHgf40'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
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
        bot.send_message(callback.message.chat.id, 'Вы выбрали экскурсию поэтапноно. \nДавайте начнем: ')
        sleep(2)
        bot.send_message(callback.message.chat.id, 'Давайте начнеч с 0 этажа. Пожалуйста спуститесь по лестницам.')
        file = open('ail_under3.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file)
        sleep(4)
        bot.send_message(callback.message.chat.id, 'Поверните налево и вы сможете увидеть столовую, а раздевалки слево от вас.')
        file = open('ail_under1.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file)
        sleep(4)
        bot.send_message(callback.message.chat.id, 'Можете развернуться и там будут 2 класса, один кабинет IT,  а второй кабинет Музыки.')
        file = open('ail_under2.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, file)
    elif callback.data == 'choice':
        bot.send_message(callback.message.chat.id, 'Вы выбрали экскурсию выборочно. \nДавайте начнем: ')
    


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/excursion - Проведем экскурсию по нашей школе! \n/wordly - игра в вордли \n/help - помощь")




if __name__ == '__main__':
    bot.polling(none_stop=True)
