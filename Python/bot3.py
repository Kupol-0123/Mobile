from mybot import *
from random import *

token("")

words = [["cat","кошка 😺"],
		 ["dog","собака 🐶"],
		 ["monkey","обезьяна 🐵"],
		 ["elephant","слон 🐘"],
		 ["fox","лиса 🦊"],
		 ["frog","лягушка 🐸"],
		 ["snake","змея 🐍"],
		 ["swan","лебедь 🦢"],
		 ["bear","медведь 🐻"],
		 ["cow","корова 🐮"],
		 ["mouse","мышь 🐭"],
		 ["rhino","носорог 🦏"],
		 ["camel","верблюд 🐫"],
		 ["kangaroo","кенгуру 🦘"],
		 ["lizard","ящерица 🦎"],
		 ["rabbit","кролик 🐇"],
		 ["rat","крыса 🐀"],
		 ["hedgehog","еж 🦔"],
		 ["turtle","черепаха 🐢"],
		 ["owl","сова 🦉"],
		 ["eagle","орел 🦅"],
		 ["parrot","попугай 🦜"],
		 ["spider","паук 🕷"],
		 ["butterfly","бабочка 🦋"],
		 ["bat","летучая мышь 🦇"],
		 ["bee","пчела 🐝"]]


users = {}

@handle
def test(ID,name,text):
	if not ID in users:
		users[ID] = {"score":0, "word":None}
		send(ID, "Привет, %s!😀 Сыграем в игру. Я буду называть слова на английском, а ты будешь переводить на русский." % name)
	if users[ID]["word"]!=None:
		if text==users[ID]["word"]:
			users[ID]["score"] += 1
			send(ID, "Правильно!😀 У тебя %d очков."%users[ID]["score"])
		else:
			send(ID, "Нет😞. Попробуй еще раз.")
	if users[ID]["word"]==None or text==users[ID]["word"]:	
		word = choice(words)
		users[ID]["word"] = word[1]
		var1 = choice(words)
		var2 = choice(words)
		var3 = choice(words)
		options = [word[1],var1[1],var2[1],var3[1]]
		shuffle(options)
		send(ID, "Переведи слово *%s*"%word[0], options)
	

start()
