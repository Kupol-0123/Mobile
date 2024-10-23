import pgzrun
WIDTH = 500
HEIGHT = 500
x = 100
y = 0
l = 200
m = 0
alive = True
def update(dt):
	global y,m
	y = y + 100*dt
	m = m + 75*dt
def draw():
	screen.fill((10,20,30))
	if alive:
		screen.draw.filled_circle((x,y),50,(100,100,100))
		screen.draw.text("1",center=(x,y),fontsize=64,color=(250,250,250))
		screen.draw.filled_circle((l,m),25,(100,200,100))

def on_mouse_down(pos):
	global alive
	if x - 50<pos[0]<x+50 and y-50<pos[1]<y+50 or l - 25<pos[0]<x+25 and m-25<pos[1]<y+25:
		alive = False
pgzrun.go()