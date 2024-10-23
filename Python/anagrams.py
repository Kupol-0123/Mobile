import pgzrun
import random
WIDTH = 500
HEIGHT = 500
words = "ЛОШАДЬ КРОВАТЬ КОРОВА".split()

def new_word():
	global word,anagram,answer,win
	word = words[random.randrange(len(words))]
	anagram = list(word)
	for _ in range(100):
		i,j = random.randrange(len(anagram)),random.randrange(len(anagram))
		anagram[i],anagram[j] = anagram[j],anagram[i]
	answer = []
	win = 0

def draw():
	screen.fill((10,20,30))
	for i in range(len(anagram)):
		if not i in answer:
			screen.draw.text(anagram[i],center=(100+50*i,100),fontsize=100)
	for i in range(len(answer)):
		screen.draw.text(anagram[answer[i]],center=(100+50*i,200),fontsize=100)
	if win>0:
		screen.draw.text("Верно!",center=(250,320),fontsize=100, color=(50,250,150))

def on_mouse_down(pos):
	global anagram,answer,win
	for i in range(len(anagram)):
		if abs(100+50*i-pos[0])<25 and abs(100-pos[1])<50 and not i in answer:
			answer.append(i)
	for i in range(len(answer)):
		if abs(100+50*i-pos[0])<25 and abs(200-pos[1])<50:
			answer.pop(i)
	if "".join([anagram[i] for i in answer])==word:
		win = 1

def update(dt):
	global win
	if win!=0:
		win = win - dt
		if win<=0:
			new_word()


new_word()
pgzrun.go()
