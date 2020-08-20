import pygame
pygame.init()
class Barrier:
	def __init__(self,x,y,bw,bh,screen,color=(30,30,30)):
		self.x=x
		self.y=y
		self.bw=bw
		self.bh=bh
		self.screen=screen
		self.color=color
	def show(self):
		pygame.draw.rect(self.screen,self.color,pygame.Rect(self.x*self.bw,self.y*self.bh,self.bw,self.bh))