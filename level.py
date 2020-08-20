import pygame
from barrier import Barrier
import pickle
import os
import os.path
import shutil
pygame.init()

class primitiveBarrier:
	def __init__(self,x,y,color=(30,30,30)):
		self.x=x
		self.y=y
		self.color=color

class level:

	def __init__(self,index,epx,epy,barrList,blockyStartX,blockyStartY):
		self.index=index
		self.barrList=barrList
		self.epx=epx
		self.epy=epy
		self.blockyStartX=blockyStartX
		self.blockyStartY=blockyStartY
		self.fileName="blockyGameLevel"#plus Index
	


class levelManager:

	
	def saveLevel(self,level):
		print("current_dir: {}".format(os.getcwd()))
		
		cur_path = os.path.dirname(__file__)

		new_path = os.path.relpath('./levels', cur_path)
		
		contents=os.listdir(new_path)
		print(contents," :contents")
		newIndex=0
		for i in contents:
			if int(i[15:])>int(newIndex):
				newIndex=int(i[15:])
				print(str(int(newIndex)+1),"= newIndex")
		with open(new_path+"/"+level.fileName+str(int(newIndex)+1),"wb") as inputFile:
			pickle.dump(level,inputFile)
			#print("savedFile to ",new_path+"/",level.fileName+newIndex)
		
		

	def createLevel(self,manualInput):
		if manualInput:	
			barriers=[]
			print("How many Barriers you want to add?")
			amountBarriers=input()
			for i in range(int(amountBarriers)):
				print("x:")
				barrierX=input()
				print("y:")
				barrierY=input()
				barriers.append(primitiveBarrier(barrierX,barrierY))#barrierX,barrierY
			print("now enter blocky start point x and y:")
			print("X:")
			blockyStartX=input()
			print("Y:")
			blockyStartY=input()

			print("now the endpoint x and y:")
			print("X:")
			epx=input()
			print("Y:")
			epy=input()
			
			newLevel=level(-1,epx,epy,barriers,blockyStartX,blockyStartY)
			self.saveLevel(newLevel)


	def loadLevel(self,index,levelPrefix):
		cur_path = os.path.dirname(__file__)

		new_path = os.path.relpath('./levels', cur_path)
		
		if os.path.exists(new_path+"/"+levelPrefix+str(index)):
			with open(new_path+"/"+levelPrefix+str(index),"rb") as outputFile:#error with path to be fixed
				level=pickle.load(outputFile)
			return level.index,level.epx,level.epy,level.barrList,level.blockyStartX,level.blockyStartY
		else:
			print("you have played through all the levels, lol")
			return False
