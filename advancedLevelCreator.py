import pygame
from level import level
from level import primitiveBarrier
pygame.init()

class AdvancedLevelCreator:
	def __init__(self,Width,Height,bw,bh,lvlManager,screen):
		self.width=Width
		self.height=Height
		self.bw=bw
		self.bh=bh
		self.lvlManager=lvlManager
		self.screen=screen
	


	def temporarilyShow(self,tempx,tempy,color):
		pygame.draw.rect(self.screen,color,(tempx*self.bw,tempy*self.bh,self.bw,self.bh))

	def createAdvancedLevel(self,event):
		#start creating level if event.type=K_u also stop when it is u
		#print("inside cal function and about to init new queque")
		exitLoop=False
		storedValues=[]
		tempClock=pygame.time.Clock()
		counter=0
		while not exitLoop:
			
			tempClock.tick(60)
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					pygame.quit()
					exit()
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_q:
						print("Stop loop")
						print(storedValues)
						exitLoop=True
				if event.type==pygame.MOUSEBUTTONDOWN:
					print("mouse down")
					if pygame.mouse.get_pos()[0]<self.width and pygame.mouse.get_pos()[1]<self.height:
						storedValues.append(primitiveBarrier(int(pygame.mouse.get_pos()[0]/self.bw),int(pygame.mouse.get_pos()[1]/self.bh)))
						tempx=int(pygame.mouse.get_pos()[0]/self.bw)
						tempy=int(pygame.mouse.get_pos()[1]/self.bh)
						if counter==0:
							self.temporarilyShow(tempx,tempy,(100,255,100))
						elif counter==1:
							self.temporarilyShow(tempx,tempy,(255,100,100))
						else:
							self.temporarilyShow(tempx,tempy,(30,30,30))
						pygame.display.flip()
						counter+=1
		#now do sth with the data
		barriersArray=[]
		#[storedValues[i] for i in range(2,len(storedValues)-1)]
		for i in range(2,len(storedValues)-1):
			barriersArray.append(storedValues[i])
			print("appended ")
		
		print("Array:  ",barriersArray)


		newLevel=level(-1,storedValues[1].x,storedValues[1].y,barriersArray,storedValues[0].x,storedValues[0].y)
		self.lvlManager.saveLevel(newLevel)