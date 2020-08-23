
class Compiler:
	'''
	syntax: whileNot(){...}
	syntax:if and ifnot{}
	maybe also var1 and var2 
	'''
	def __init__(self,moveTimesFunction,blockyCharacter):
		self.moveTimesFunction=moveTimesFunction
		self.blocky=blockyCharacter


	def moveDown(self,n):
		self.moveTimesFunction(0,1,n)
	def moveUp(self,n):
		self.moveTimesFunction(0,-1,n)
	def moveLeft(self,n):
		self.moveTimesFunction(-1,0,n)
	def moveRight(self,n):
		self.moveTimesFunction(1,0,n)
	
	def compile(self,text,barriers):
		def update():
			self.blocky.adjustAttributes(barriers)
		isBarrierTop=self.blocky.isBarrierTop
		isBarrierLeft=self.blocky.isBarrierLeft
		isBarrierRight=self.blocky.isBarrierRight
		isBarrierBottom=self.blocky.isBarrierBottom
		isFinished=self.blocky.isFinished# i have to update those
		try:
			exec(text,{},{"isFinished":isFinished,"isBarrierBottom":isBarrierBottom,"isBarrierRight":isBarrierRight,"isBarrierLeft":isBarrierLeft,"isBarrierTop":isBarrierTop,"md":self.moveDown,"mu":self.moveUp,"ml":self.moveLeft,"mr":self.moveRight,"updt":update})
		except:
			print("Syntax Error")
		
































	def oldCompile(self,text):
		print(text)
		for i in range(len(text)):#iterate through entire code
			#print("i: {} char: {}".format(i,text[i]))
			try:
				if text[i]=="(":#here happens the checking for (
					if i > 1:
						#print(text[i-2:i])
						if text[i-2:i]=="ml":#would incliude i-3 and i-1
							j=i
							n=""
							while(not text[j+1]==")"):
								
								try:
									n+=str(int(text[j+1]))
								
								except:
									print("Arguments must be numeric")
								j+=1
							self.moveTimesFunction(-1,0,int(n))
							
						elif text[i-2:i]=="mu":#would incliude i-3 and i-1
							j=i
							n=""
							while(not text[j+1]==")"):
								
								try:
									n+=str(int(text[j+1]))
								
								except:
									print("Arguments must be numeric")
								j+=1
							self.moveTimesFunction(0,-1,int(n))
							
						elif text[i-2:i]=="md":#would incliude i-3 and i-1
							j=i
							n=""
							while(not text[j+1]==")"):
								try:
									n+=str(int(text[j+1]))
								
								except:
									print("Arguments must be numeric")
								j+=1
							self.moveTimesFunction(0,1,int(n))
							
						elif text[i-2:i]=="mr":#would incliude i-3 and i-1
							j=i
							n=""
							while(not text[j+1]==")"):
								
								try:
									n+=str(int(text[j+1]))
								
								except:
									print("Arguments must be numeric")
								j+=1
							
							self.moveTimesFunction(1,0,int(n))
								
						else:
							print("syntax error")
			except Exception:
				print("Code couldnt be compiled")