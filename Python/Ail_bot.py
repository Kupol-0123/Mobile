from mybot import *
from random import *

token("8001281886:AAGB1apo5WMuBr1VBDQYyESCGg-rOTHgf40")

users = {}

@handle
def test(ID,name,text):
	if not ID in users:
		send(ID, f"Здраствуйте {name}! Добро пожаловать в школу AIL. Давайте проведем экскурсию. Сначала начнем с 1 этажа.")
		send(ID,"Пройдите после входа налево и увидете кабинеты. Можете осмотреться там есть младшие классы.")
		pic = '[url=https://ibb.co/FXVCHM0][img]https://i.ibb.co/FXVCHM0/305468393-550472946885298-6627952138906825461-n.jpg[/img][/url]'
		send_pic(ID,pic)

start()