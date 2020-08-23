import pygame
import ptext


class inputBox:

    def __init__(self,textx,texty,x,y,w,h,colorText,colorFrame,text="Ins."):
        import pygame
        self.colorText=colorText
        self.colorFrame=colorFrame
        self.font=pygame.font.SysFont('Arial', 20)
        #self.rect=pygame.rect(x,y,w,h)
        self.textx=textx
        self.texty=texty
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.accessText=False
        self.text=text
        self.myText=None
        print("inited box")
    
   
    def addNewLine(self):
        self.text+="\n"
    def display(self,screen):
        #Drawing box around Text
        pygame.draw.rect(screen,self.colorFrame,pygame.Rect(self.x,self.y,self.w,self.h))
        #Drawing Text hopefully inside box
        #myText=self.font.render(self.text,True,self.colorText)
        #screen.blit(myText,(self.textx,self.texty))
       
        ptext.draw(self.text,(self.textx,self.texty))
    def sendText(self):
        return self.text

    def addText(self,event,func):
        if event.key==pygame.K_BACKSPACE:
            self.text=self.text[:-1]
        elif event.key==pygame.K_RETURN:
            self.addNewLine()
        else:
            self.text+=event.unicode
            self.myText=self.font.render(self.text,True,self.colorText)


