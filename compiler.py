
class Compiler:
	'''
	syntax: whileNot(){...}
	syntax:if and ifnot{}
	maybe also var1 and var2 
	'''
	def __init__(self,moveTimesFunction):
		self.moveTimesFunction=moveTimesFunction
		#self.commands={"ml":lambda n:self.moveTimesFunction(-1,0,n),"md":}
	def moving(self,text,coords,cursorpos):
		i=cursorpos
		while text[i]:
			pass

	
	def compile(self,text):
		movingDictionary={"ml":(-1,0),"mu":(0,-1),"mr":(1,0),"md":(0,1)}
		loopAndIfDictionary={"if":self.ifFunction,"ifnot":self.ifNotFunction,"while":self.whileFunction,"whilenot":self.whileNotFunction}
		copyOfText=text
		inLoop1=False
		inLoop2=False
		inLoop3=False
		for i in range(len(text)):#loops through entire text
			
			for key in movingDictionary:#this is just Moving,not loop nor if or ifnot
				if key==text[i:i+len(key)]:#maybe i-1
					if key=="mu":
						moveTimesFunction(movingDictionary[key])
			for key in loopAndIfDictionary:
				if key==text[i:i+len(key)]:
					print("imagine my code executing",key,"now.")

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