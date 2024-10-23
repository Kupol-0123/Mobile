import pgzrun
import random
import numpy
WIDTH = 680
HEIGHT = 300
words = ['НУЛЬ','АРБУЗ','ЛОШАДЬ','КОРОВА','КНОПКА','ТЕЛЕГА','ИГРОК','ЛОЖКА','ДЕРЕВО']


def restart():
	global a,b,win,timer,word
	word = random.choice(words)
	a = list(numpy.random.permutation(list(word)))
	b = []
	win = False
	timer = 0


def update(dt):
	global win, timer
	print(''.join([a[i] for i in b]),word,win)
	if ''.join([a[i] for i in b])==word:
		win = True
	if win:
		timer = timer + dt
	if timer>1:
		restart()


def draw():
	screen.blit('desk',(0,0))
	for i in range(len(a)):
		if not i in b:
			screen.blit(str(ord(a[i])),(20+i*80,30))
	for j in range(len(b)):
		screen.blit(str(ord(a[b[j]])),(20+j*80,150))
	if win:
		screen.blit('win',(0,0))


def on_mouse_down(pos):
	global a, b
	for i in range(len(a)):
		if 20+i*80<pos[0]<100+i*80 and 30<pos[1]<150 and not i in b:
			b.append(i)
	for j in range(len(b)):
		if 20+j*80<pos[0]<100+j*80 and 150<pos[1]<270:
			b.pop(j)

restart()
pgzrun.go()
