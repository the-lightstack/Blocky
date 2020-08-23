class blockyCharacter:
	def __init__(self,x,y,stepsizexy,color=(200,200,200)):
		self.x=x
		self.y=y
		self.stepsizexy=1
		self.color=color

		self.isBarrierTop=None
		self.isBarrierRight=None
		self.isBarrierLeft=None
		self.isBarrierBottom=None
		self.isFinished=False
	def move(self,x,y):
		self.x+=x
		self.y+=y

	def adjustAttributes(self,barriers):
		#check for the right side of blocky
		ibr=False
		for i in barriers:
			if self.x+1==i.x and self.y==i.y:
				ibr=True
				break
		ibt=False
		for i in barriers:
			if self.x==i.x and self.y-1==i.y:
				ibt=True
				break
		ibb=False
		for i in barriers:
			if self.x==i.x and self.y+1==i.y:
				ibb=True
				break
		ibl=False
		for i in barriers:
			if self.x-1==i.x and self.y==i.y:
				ibl=True
				break
		self.isBarrierBottom=ibb
		self.isBarrierLeft=ibl
		self.isBarrierRight=ibr
		self.isBarrierTop=ibt



