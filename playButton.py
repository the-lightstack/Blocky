import pygame
import os
import os.path
import shutil

pygame.init()
class playButton:
	manualMoving=False
	def __init__(self,x,y,w,h,compiler,path,screen):
		self.x=x
		self.y=y
		self.w=w
		self.h=h
		self.compiler=compiler
		self.path=path
		self.image=None
		
		self.screen=screen

	def loadImage(self):
		print("At playButton class: curren directory={} ".format(os.getcwd()))
		self.image=pygame.image.load(self.path)

	def initButton(self):
		self.loadImage()
		self.image = pygame.transform.scale(self.image, (self.w, self.h))
	
	def buttonClicked(self,event):
		#collidepoint
		if event.type==pygame.MOUSEBUTTONDOWN:

			if pygame.Rect(self.x,self.y,self.w,self.h).collidepoint(pygame.mouse.get_pos()):
				print("clicked")
				return True
	def executeFunction(self,event,text):
		
		if self.buttonClicked(event):
			print("debug inside")
			if callable(self.compiler):
				self.compiler()
			else:
				#self.compiler.oldCompile(text)
				self.compiler.compile(text)
	def show(self):
		self.screen.blit(self.image,(self.x,self.y))

