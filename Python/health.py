import pgzrun,random
WIDTH = 501
HEIGHT = 501

mass = [[random.randint(0, 1) for _ in range(50)] for _ in range(50)]
timer = 1

def draw():
	screen.fill((10,10,10))
	for x in range(50):
		for y in range(50):
			screen.draw.filled_rect(Rect((x*10,y*10),(10,10)),
				(200,200,200)if mass[x][y]==1 else (50,50,50))
			screen.draw.rect(Rect((x*10,y*10),(11,11)),(100,100,100))

def update(dt):
	global timer
	timer = timer - dt
	if timer < 0.92:
		timer = 1
		neib = [[0 for _ in range(50)]for _ in range(50)]
		for x in range(-1,49):
			for y in range(-1,49):
				n = 0
				if mass[x+1][y]==1:
					n = n+1
				if mass[x-1][y]==1:
					n = n+1
				if mass[x][y+1]==1:
					n = n+1
				if mass[x][y-1]==1:
					n = n+1
				if mass[x+1][y+1]==1:
					n = n+1
				if mass[x+1][y-1]==1:
					n = n+1
				if mass[x-1][y+1]==1:
					n = n+1
				if mass[x-1][y-1]==1:
					n = n+1
				neib[x][y] = n
		for x in range(50):
			for y in range(50):
				if mass[x][y]==1 and (neib[x][y]<2 or neib[x][y]>3):
					mass[x][y] = 0
				if mass[x][y]==0 and (neib[x][y]>2 and neib[x][y]<4):
					mass[x][y] = 1




pgzrun.go()
