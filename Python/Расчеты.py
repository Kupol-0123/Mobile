import pgzrun, random
WIDTH = 500
HEIGHT = 500

def restart():
	global ball, l, x, y, timer
	ball = False
	l = 4
	x = [random.randint(10, 490) for _ in range(l)]
	y = [random.randint(10, 490) for _ in range(l)]
	timer = random.randint(1, 3)

def draw():
	screen.fill((15,10,10))
	if ball:
		for m in range(l):
			screen.draw.filled_circle((x[m],y[m]),8,(255,255,255))

def update(dt):
	global timer,ball
	if ball == False:
		timer = timer - dt
	if timer <= 0.0:
		ball = True

def on_mouse_down(pos):
	global ball, x, y
	if ball:
		if x[m]<pos[0]<y[m] and x[m]<pos[1]<y[m]:
			pass


restart()
pgzrun.go()
