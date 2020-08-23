import pygame
import os
import os.path
import shutil

pygame.init()
class EndPoint:
	def __init__(self,x,y,bw,bh,screen,path,blocky):
		self.x=x
		self.y=y
		self.bw=bw
		self.bh=bh
		self.screen=screen
		self.path=path
		self.image=None
		self.rect=pygame.Rect(x,y,bw,bh)
		self.blocky=blocky
	
	def initEndPoint(self):
		self.image=pygame.image.load(self.path)
		self.image = pygame.transform.scale(self.image, (self.bw, self.bh))

	def show(self):
		self.screen.blit(self.image,(self.x*self.bw,self.y*self.bh))

	def checkCollision(self,blocky,functionNL,parameter,endpoint):
		if blocky.x==self.x and blocky.y==self.y:
			blocky.isFinished=True
			functionNL(parameter,blocky,endpoint)
			print("you won!")
			return True



