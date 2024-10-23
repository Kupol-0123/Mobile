import pgzrun
import random
WIDTH = 500
HEIGHT = 500
difficult_level = 0
win = False


def restart():
	global menu,ball,posi, F, x,y,difficult_menu, eazy, hard, normal, health, speed, l, win,timer
	difficult_menu = False
	menu= True
	ball=0
	win= False
	speed = 80
	health = [3,5,6][difficult_level]
	posi= 170
	timer=0
	F = False
	l = [1,3,5][difficult_level]
	x = [random.randint(10, 490) for _ in range(l)]
	y = [random.randint(-300,60) for _ in range(l)]

def on_mouse_down(pos):
	global menu, F, x, y, difficult_menu, eazy,normal,hard,speed, health,l, difficult_level
	if menu:
		if 150<pos[0]<350 and 250<pos[1]<300:
			menu = False
			F = True
		if 150<pos[0]<350 and 320<pos[1]<370:
			difficult_menu = True
		if difficult_menu:
			if 150<pos[1]<350 and 130<pos[1]<180:
				difficult_level = 0
				difficult_menu = False
				restart()
			if 150<pos[1]<350 and 200<pos[1]<250:
				difficult_level = 1
				health = 5
				difficult_menu = False
				restart()
			if 150<pos[1]<350 and 270<pos[1]<320:
				difficult_level = 2
				health = 6
				difficult_menu = False
				restart()
		
def update(dt):
	global x,y,ball, speed, health, l,timer,win,menu
	speed = [80,90,120][difficult_level]
	if menu == False and win ==False:
		print(timer)
		for i in range(l):
			y[i] = y[i] + (speed+ball)*dt
			if 350<y[i]<380 and posi<x[i]<posi+150:
				ball= ball+1
				if ball%20==0:
					health= health+1
				x[i] = random.randint(0, 500)
				y[i] = 20		
				if ball >= 100:
					win= True
					timer = 2	
			if y[i] >= 500:
				health = health-1
				x[i] = random.randint(0, 500)
				y[i] = 20	
				if health == 0:
					restart()
	if win:
		timer = timer - dt
		if timer<0:
			win = False
			menu = True



def draw():
	if menu == False:
		screen.blit('desk',(0,0))
		JOL = 244, 164, 96
		HEL = Rect((posi,350),(150,30))
		screen.draw.filled_rect(HEL,JOL)
		screen.draw.text(f"Баллы: {ball}",(160,400), color='yellow',fontsize=50)
		screen.draw.text(f"Жизни: {health}",(150,450), color='yellow',fontsize=60)
		if F:
			for m in range(l):
				screen.draw.filled_circle((x[m],y[m]),5,(255,255,255))
	else:
		screen.blit('menu',(0,0))
		RED = 135, 206, 235
		BOX = Rect((150,250), (200,50))
		FI = 135, 206, 235
		DIFFICULT = Rect((150,320), (200,50))
		screen.draw.filled_rect(BOX,RED)
		screen.draw.filled_rect(DIFFICULT,FI)
		screen.draw.text("Начало", (180,250), color='white',fontsize=60)
		screen.draw.text("Сложность", (160,330), color='white',fontsize=50)
		screen.draw.text("Игра в Ловителя", (100,40), color='orange',fontsize=60)
	if win and not menu:
		screen.draw.text("Победа",(130,80), color='green',fontsize=90)
	if difficult_menu:
		screen.blit('menu',(0,0))
		GREEN = 0, 255, 127
		EAZY = Rect((150,130), (200,50))
		screen.draw.filled_rect(EAZY,GREEN)
		screen.draw.text("Легкий", (180,140), color='white',fontsize=60)
		ORANGE = 255, 215, 0
		NORMAL = Rect((150,200), (200,50))
		screen.draw.filled_rect(NORMAL,ORANGE)
		screen.draw.text("Средний", (160,205), color='white',fontsize=60)
		RED = 255, 69, 0
		HARD = Rect((150,270), (200,50))
		screen.draw.filled_rect(HARD,RED)
		screen.draw.text("Сложный", (150,275), color='white',fontsize=60)

def on_key_down(key):
	global posi,menu
	if key==keys.A: 
		for i in range(5):
			posi=posi-10
	if posi<=0:
			posi = 0
	if key==keys.D: 
		for i in range(5):
			posi = posi+10
		if posi>=350:
			posi =350
	if key==keys.LEFT: 
		for i in range(5):
			posi=posi-10
	if posi<=0:
			posi = 0
	if key==keys.RIGHT: 
		for i in range(5):
			posi = posi+10
		if posi>=350:
			posi =350


restart()
pgzrun.go()