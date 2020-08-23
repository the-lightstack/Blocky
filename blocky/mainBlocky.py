
import pygame
from time import sleep

from blockyCharacter import blockyCharacter
from barrier import Barrier

from inputBox import inputBox
from playButton import playButton

from endPoint import EndPoint

from level import levelManager,level#remove level class import later

from advancedLevelCreator import AdvancedLevelCreator

from compiler import Compiler

pygame.init()
#------ Variables ----

columns=15
rows=10
clock=pygame.time.Clock()
gridColor=(100,100,100)

#manualMoving=False
currentLevel=0
barriers=[]

FRAMEWIDTH=1100
FRAMEHEIGHT=400
WIDTH=600 
HEIGHT=FRAMEHEIGHT
FPS=60
BOXWIDTH=int(WIDTH/columns)
BOXHEIGHT=int(HEIGHT/rows)
FONT=pygame.font.Font(None,32)


#---- Setup -----
screen=pygame.display.set_mode((FRAMEWIDTH,FRAMEHEIGHT))
pygame.display.set_caption("BlockyIns")
gameRunning=True


#---- Functions ------
def drawGrid():
	for i in range(columns):
			pygame.draw.line(screen,gridColor,(int(i*WIDTH/columns),0),(int(i*WIDTH/columns),HEIGHT))

	for j in range(rows):
		pygame.draw.line(screen,gridColor,(0,int(j*HEIGHT/rows)),(WIDTH,int(j*HEIGHT/rows)))


def makeDesign(colorSplit,colorBackground,thickness):
	pygame.draw.line(screen,colorSplit,(columns*BOXWIDTH+int(thickness/2),0),(columns*BOXWIDTH+int(thickness/2),HEIGHT),thickness)
	pygame.draw.rect(screen,colorBackground,pygame.Rect((columns*BOXWIDTH+int(thickness),0),(FRAMEWIDTH-WIDTH-thickness,FRAMEHEIGHT)))


def drawBlocky(blocky):
	pygame.draw.rect(screen,blocky.color,pygame.Rect((int(blocky.x*BOXWIDTH),int(blocky.y*BOXHEIGHT)),(BOXWIDTH,BOXHEIGHT)))



def moveValid(blocky,x,y,barriers):#checking for all evil
	valid=True
	if blocky.x+x<0 or blocky.x+x>columns-1 or blocky.y+y>rows-1 or blocky.y+y<0:
		valid=False
	for i in barriers:
		if blocky.x+x ==i.x and blocky.y+y == i.y:
			valid=False
	if valid:
		return True
	else:
		print("Invalid move: Stop doing that")
		return False
			
	

def moveNTimes(x,y,n):
	if n<100:
		for i in range(n):
			if moveValid(blocky,x,y,barriers):
				sleep(0.2)
				blocky.move(x,y)
				drawBlocky(blocky)
				#add draw screen and grid to remove snake look of blocky
				pygame.display.flip()




			
def changeGameState(blocky,endPoint,inputs):
	
	
	blocky.x=int(inputs[4])
	
	blocky.y=int(inputs[5])
	
	endPoint.x=int(inputs[1])
	
	endPoint.y=int(inputs[2])
	

	
	for i in inputs[3]:	
		barriers.append(Barrier(int(i.x),int(i.y),BOXWIDTH,BOXHEIGHT,screen))

def nextLevel(lvlManager,blocky,endpoint):
	
	global barriers
	barriers=[]
	
	global currentLevel
	currentLevel+=1
	output=lvlManager.loadLevel(currentLevel,"blockyGameLevel")
	if output!=False:
		changeGameState(blocky,endpoint,output)
		print("success")
	else:
		print("Error, output not existing because of no levels")

def changeMM():
	playButton.manualMoving= not playButton.manualMoving



#------  Init character -------


blocky=blockyCharacter(1,1,1,(27,77,62))

myCompiler=Compiler(moveNTimes,blocky)

box=inputBox(WIDTH+50,75,WIDTH+25,50,400,200,(0,0,0),(150,130,132))

play=playButton(WIDTH+50,270,117,50,myCompiler,"PlayButtonBlockyGame.png",screen)

myEndPoint=EndPoint(0,9,BOXWIDTH,BOXHEIGHT,screen,"endPointImage.png",blocky)

manualMovingButton=playButton(WIDTH+400,270,40,40,changeMM,"manualMovingButton.png",screen)

lvlManager=levelManager()

advancedCreator=AdvancedLevelCreator(WIDTH,HEIGHT,BOXWIDTH,BOXHEIGHT,lvlManager,screen)

#------ Mainloop -----
play.initButton()
manualMovingButton.initButton()


myEndPoint.initEndPoint()


screen.fill((100,100,200))
drawGrid()
makeDesign((27,24,17),(191,175,178),5)

#lvlManager.createLevel(True)


	

nextLevel(lvlManager,blocky,myEndPoint)

def mainLoop():
	blocky.adjustAttributes(barriers)
	screen.fill((100,100,200))
	drawGrid()
	makeDesign((27,24,17),(191,175,178),5)
	box.display(screen)
	manualMovingButton.show()
	play.show()
	
	myEndPoint.show()
	myEndPoint.checkCollision(blocky,nextLevel,lvlManager,myEndPoint)
	drawBlocky(blocky)
	
	for i in barriers:
		
		i.show()
	
	
while gameRunning:
	clock.tick(FPS)
	mainLoop()	
	pygame.display.flip()
	








	#--- Event handling -----

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			gameRunning=False
		if event.type==pygame.MOUSEBUTTONDOWN:
			play.executeFunction(event,box.text,barriers)
			manualMovingButton.executeFunction(event,box.text,barriers)
			
		if event.type==pygame.KEYDOWN:
			if not playButton.manualMoving:
				box.addText(event,compile)
			if event.key==pygame.K_q:
				#print("o was pressed and advanced Creator will be opened")
				advancedCreator.createAdvancedLevel(event)
			if playButton.manualMoving:#manual moving means you can directly control the character 
				if event.key==pygame.K_d:
					if moveValid(blocky,1,0,barriers):
						blocky.move(1,0)
				elif event.key==pygame.K_a:
					if moveValid(blocky,-1,0,barriers):
						blocky.move(-1,0)
				elif event.key==pygame.K_w:
					if moveValid(blocky,0,-1,barriers):
						blocky.move(0,-1)
				elif event.key==pygame.K_s:
					if moveValid(blocky,0,1,barriers):
						blocky.move(0,1)
				else:
					print("Error Code 105: Invalid input Error raised")

	
	

