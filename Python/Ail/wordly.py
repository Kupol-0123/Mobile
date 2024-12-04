from telebot import *
from time import *
from random import *

API_TOKEN = '6772366285:AAHHUhoHjYWpUfldWee_lnQQh5ENFpV6fjm'
bot = telebot.TeleBot(API_TOKEN)

active = False

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, f"Привет {message.chat.first_name}! Давай сыграем в игру водли!")
    bot.send_message(message.chat.id, "Тебе будет загадоно слово и ты должен будешь отгадать. \n Напиши /begin - чтобы начать игру.")


@bot.message_handler(commands=['begin'])
def wordly(message):
    global word, i, unword, word_back, active, iol
    words = "завод навоз сосна мячик замок актёр банан барин барка бисер благо бомба бурка валет варка вилка виски ворон груша думка".split()
    word = choice(words).upper()
    word = list(word)
    word_back = "".join(word)
    word_back = word_back.capitalize()
    i = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
    iol = -1
    unword = ['_' for _ in range(30)]
    bot.send_message(message.chat.id, f'{unword[0]} {unword[1]} {unword[2]} {unword[3]} {unword[4]} \n{unword[5]} {unword[6]} {unword[7]} {unword[8]} {unword[9]} \n{unword[10]} {unword[11]} {unword[12]} {unword[13]} {unword[14]} \n{unword[15]} {unword[16]} {unword[17]} {unword[18]} {unword[19]} \n{unword[20]} {unword[21]} {unword[22]} {unword[23]} {unword[24]}')
    bot.send_message(message.chat.id, 'Введите слово: ')
    active = True
    bot.register_next_step_handler(message, start_game)

def start_game(message):
    global iol, active
    if active:
        iol = iol + 1
        input_word = message.text.upper()
        if len(input_word) > 5 or len(input_word) < 5:
            bot.send_message(message.chat.id, 'Ваше слово больше или меньше 5 букв!!')
            bot.send_message(message.chat.id, 'Введите слово: ')
            iol = iol - 1
            bot.register_next_step_handler(message, start_game)
        else:
            input_word = list(input_word)
            for b in range(0,5):
                unword[i[iol][b]] = input_word[b]
                for p in range(0,5):
                    if b == p:
                        if input_word[b] == word[b]:
                           unword[i[iol][b]] = input_word[b].upper()
                           break
                    elif input_word[b] == word[p]:
                        unword[i[iol][b]] = input_word[b].lower()
                        break
                    elif input_word[b] != word[p]:
                        unword[i[iol][b]] = '_'
            bot.send_message(message.chat.id, f'{unword[0]} {unword[1]} {unword[2]} {unword[3]} {unword[4]} \n{unword[5]} {unword[6]} {unword[7]} {unword[8]} {unword[9]} \n{unword[10]} {unword[11]} {unword[12]} {unword[13]} {unword[14]} \n{unword[15]} {unword[16]} {unword[17]} {unword[18]} {unword[19]} \n{unword[20]} {unword[21]} {unword[22]} {unword[23]} {unword[24]}')
            bot.send_message(message.chat.id, 'Введите слово: ')
            bot.register_next_step_handler(message,start_game)  
            if input_word == word:
                bot.send_message(message.chat.id,f"Поздравляем! Вы угадали слово, загоданое слово было: <b>{word_back}</b>", parse_mode="HTML")
                active = False
            elif iol == 4:
                bot.send_message(message.chat.id,f"К сожелению вы не угадали слова, загоданое слово было: <b>{word_back}</b>", parse_mode="HTML")
                active = False


@bot.message_handler(content_types=['text'])
def fffff(message):
    bot.send_message(message.chat.id, "Напиши /begin - чтобы начать игру.")

if __name__ == '__main__':
    bot.polling(none_stop=True)
