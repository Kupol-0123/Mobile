from telebot import *
from time import *

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, f"Здраствуйте {message.chat.first_name}! Добро пожаловать в школу AIL. Что вы хотите бы узнать?")
    bot.send_message(message.chat.id, "/excursion - Проведем экскурсию по нашей школе! \n/play - поиграть в Викторину.  \n/history - история с развитием событий. \n/help - помощь")
    def send_photo(message):
        with open('AIL_Start.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    send_photo(message)

# @bot.message_handler(content_types=['text'])
# def history(message):
#     if message.text == '/history':
#         bot.send_message(message.chat.id, "Загадка Лесного Убежища.")
#         sleep(2)
#         bot.send_message(message.chat.id,"Ты и твои друзья отправляетесь в лес на выходные. Легенда гласит, что в его глубине скрыто таинственное убежище, охраняемое загадками и испытаниями. Ваше приключение начинается у старого дуба, у которого лежит старинная карта. На карте обозначены три пути:")
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         item1 = types.KeyboardButton("Тропа Ветров")
#         item2 = types.KeyboardButton("Тропа Теней")
#         item3 = types.KeyboardButton("Тропа Солнца")
#         markup.add(item1, item2, item3)
#         bot.send_message(message.chat.id,"Выберите путь:" , reply_markup=markup)
#     if message.text == 'Тропа Ветров':
#         bot.send_message(message.chat.id,"Ты идешь вдоль реки, когда вдруг появляется водяной. Он смотрит на вас с недоверием.")
#         sleep(2)
#         bot.send_message(message.chat.id,"Водяной: Чтобы пройти дальше, вы должны ответить на загадку: ")
#         sleep(0.5)
#         bot.send_message(message.chat.id,"Что никогда не возвращается, хотя всегда уходит?")
#         sleep(2)
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         var1 = types.KeyboardButton('Ответить: Время')
#         var2 = types.KeyboardButton('Сказать, что не знаешь и попытаться пройти мимо.')
#         markup.add(var1, var2)
#         bot.send_message(message.chat.id,"Ваши действия?", reply_markup=markup)
#     if message.text == 'Тропа Теней':
#         bot.send_message(message.chat.id,"Погружаясь в темный лес, ты чувствуешь, как вокруг накапливается напряжение. Вдруг перед тобой возникает темная фигура — это дух леса.")
#         sleep(2)
#         bot.send_message(message.chat.id,"Дух: Только тот, кто знает силу света, сможет пройти дальше. Назови, что светит в темноте, но не имеет формы.")
#         sleep(0.5)
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         var1 = types.KeyboardButton('Ответить: Звезды')
#         var2 = types.KeyboardButton('Попробовать сбежать от духа.')
#         markup.add(var1, var2)
#         bot.send_message(message.chat.id,"Ваши действия?", reply_markup=markup)
#     if message.text == 'Тропа Солнца':
#         bot.send_message(message.chat.id,"Ты идешь по открытой тропе, и вскоре видишь солнечное озеро. На берегу стоит старая ведьма.")
#         sleep(2)
#         bot.send_message(message.chat.id,"Ведьма: Чтобы я помогла тебе, нужно сделать выбор:")
#         sleep(0.5)
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         var1 = types.KeyboardButton('Принести мне два цветка с Тропы Теней.')
#         var2 = types.KeyboardButton('Ответить на вопрос: что может расти, но не имеет корней?')
#         var3 = types.KeyboardButton('Выбрать первый вариант.')
#         var4 = types.KeyboardButton('Ответить: Идеи')
#         markup.add(var1, var2, var3, var4)
#         bot.send_message(message.chat.id,"Ваши действия?", reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/excursion - Проведем экскурсию по нашей школе! \n/play - поиграть в Викторину.  \n/history - история с развитием событий. \n/help - помощь")


# @bot.message_handler(func=lambda message: True)
# def calculate(message):
#     try:
#         result = eval(message.text)
#         bot.send_message(message.chat.id, f"Ответ: {result}")
#     except Exception as e:
#         pass

# @bot.message_handler(commands=['play'])
# def play(message):
#     question = [["Какая планета самая большая в Солнечной системе?",]
#                ["Сколько океанов на Земле?"],
#                ["Какой цвет получается при смешивании красного и синего?"]]
#     answer = [["Земля", "Юпитер", "Сатурн", "Марс"],
#              ["3","4","5","6"],
#              ["Зелёный","Фиолетовый","Оранжевый","Жёлтый"]]
#     bot.send_message(message.chat.id,choice(question))
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     var1 = types.KeyboardButton(choice(answer))
#     var2 = types.KeyboardButton(choice(answer))
#     var3 = types.KeyboardButton(choice(answer))
#     var4 = types.KeyboardButton(choice(answer))
#     markup.add(var1, var2, var3, var4)
#     bot.send_message(message.chat.id,"Выбирете один из вариантов.", reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)
