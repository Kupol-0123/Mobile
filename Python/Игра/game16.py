import pgzrun
import numpy
WIDTH = 500
HEIGHT = 500
menu= True
timera=0
cover=False

def restart():
	global card,state,a,b,timer,win
	card = numpy.random.permutation([0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7])
	state = [0]*16
	a = None
	b = None
	timer=0
	win=False


def update(dt):
	global win, timer,a,b,cover,timera,menu
	if state==[2]*16:
		win=True
		menu=True
	if win:
		timer = timer + dt
	if timer>1:
		restart()
	if cover:
		timera=timera+dt
	if timera>1:
		state[a] = 2
		state[b] = 2
		a = None
		b = None
		timera=0
		cover=False

def draw():
	if menu == False:
		screen.blit('desk',(0,0))
		for i in range(16):
			x = 20 + 120*(i%4)
			y = 20 + 120*(i//4)
			if state[i]==0:
				screen.blit('back',(x,y))
			elif state[i]==1:
				screen.blit(str(card[i]),(x,y))
	else:
		screen.blit('desk_menu',(0,0))
		RED = 27, 203, 121
		BOX = Rect((150,240), (200,50))
		screen.draw.filled_rect(BOX,RED)
		screen.draw.text("Начало", (180,250), color='white',fontsize=60)
		screen.draw.text("Игра в 16", (150,40), color='orange',fontsize=60)


def on_mouse_down(pos):
	global a,b,k,cover,win,menu
	if menu:
		if 150<pos[0]<350 and 240<pos[1]<290:
			menu = False
	else:
		if cover==False:
			for i in range(16):
				x = 20 + 120*(i%4)
				y = 20 + 120*(i//4)
				if x<pos[0]<x+100 and y<pos[1]<y+100:
					if a==None and b==None and state[i]==0:
						a = i
						state[i] = 1
					elif a!=None and b==None and state[i]==0:
						b = i
						state[i] = 1
						if card[a]==card[b]:
							cover=True

					elif b!=None:	
						state[a] = 0
						state[b] = 0
						a = None
						b = None
restart()
pgzrun.go()
