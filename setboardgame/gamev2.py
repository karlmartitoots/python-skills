import itertools as it
from tkinter import *
import random
from PIL import Image as Img, ImageTk as ImgTk
import os

dirname = os.path.dirname(__file__)

# diamond, oval and squiggle
shapes = ["diamond","oval","squiggle"]

colors = ["red","green","purple"]

shadings = ["full","striped","empty"]

amounts = [1,2,3]

class Card(Button):
    
    def __init__(self,parent,shape,color,shading,amount,*args,**kwargs):
        self.containerWidth, self.containerHeight = 200,125
        self.shapeWidth, self.shapeHeight = 30,60
        self.distBetweenShapes = self.shapeWidth//4
        self.shape = shape
        self.color = color
        self.shading = shading
        self.amount = amount
        self.chosen = False
        self.observers = []
        self.shapeImage = self.loadImage()
        Button.__init__(self, parent, image = self.shapeImage, command = self.onClick, height = self.containerHeight, width = self.containerWidth,*args,**kwargs)
        self.origColor = self.cget("background")
        self.bind("<Enter>", self.onEnter)
        self.bind("<Leave>", self.onLeave)
        self.bind("<Button-1>", self.onClick)

    def loadImage(self):
        cardImage = Img.open(os.path.join(dirname, 'resourcesv2/'+self.shape+self.color+self.shading+str(self.amount)+'.png'))
        resizedCardImage = cardImage.resize((self.shapeWidth*self.amount + self.distBetweenShapes*(self.amount-1), self.shapeHeight), Img.ANTIALIAS)
        tkCardImage = ImgTk.PhotoImage(resizedCardImage)
        allImages.append(tkCardImage)
        return tkCardImage
    
    def addObserver(self,observer):
        self.observers.append(observer)
    
    def removeObserver(self,observer):
        self.observers.remove(observer)
    
    def notifyObservers(self):
        for obs in self.observers:
            obs.choose(self)
    
    def onEnter(self,event):
        if not self.chosen:
            self.config(bg="SkyBlue1")

    def onLeave(self,event):
        if not self.chosen:
            self.config(bg=self.origColor)

    def onClick(self):
        self.setChosen()
    
    def setChosen(self):
        self.chosen = True
        self.config(bg="tan1")
        self.notifyObservers()
    
    def setUnChosen(self):
        self.chosen = False
        self.config(bg=self.origColor)

class Board:
    
    def __init__(self, parent):
        self.cardSlots = [[None,None,None],\
                          [None,None,None],\
                          [None,None,None],\
                          [None,None,None]]
        self.chosenCards = []
        self.GL = Gamelogic()
        self.deck = Deck(parent)
        self.emptyCard = Card(parent,"empty","","",1)
        self.scoreVar = StringVar()
        self.score = 0
        self.scoreVar.set("0")
        self.scoreLabel = Label(parent, textvariable = self.scoreVar)
        self.scoreLabel.config(font=("Courier", 44))
        self.scoreLabel.grid(row=4,column=0,columnspan = 3)
    
    def setCardAt(self,col,row,card):
        self.cardSlots[row][col] = card
        self.getCardAt(col,row).grid(row=row,column=col,padx=cardPadding,pady=cardPadding)
        card.addObserver(self)
    
    def getCardAt(self,col,row):
        return self.cardSlots[row][col]
    
    def replaceCard(self, removeCard, addCard):
        for row in range(4):
            for col in range(3):
                if self.cardSlots[row][col] == removeCard:
                    self.setCardAt(col,row,addCard)
    
    def replaceChosenCards(self):
        for card in self.chosenCards:
            newCard = self.deck.takeOne()
            if newCard:    
                self.replaceCard(card, newCard)
                card.destroy()
            else:
                self.replaceCard(card, self.emptyCard)
    
    def chosenCardsInSet(self):
        return self.GL.isSet(self.chosenCards)

    def initFillSlots(self):
        for col in range(3):
            for row in range(4):
                self.setCardAt(col,row,self.deck.takeOne())
    
    def choose(self,card):
        self.chosenCards.append(card)
        if len(self.chosenCards) > 2:
            for c in self.chosenCards:
                c.setUnChosen()
            if self.chosenCardsInSet():
                print("SET!")
                self.incrementScoreVar()
                self.replaceChosenCards()
            else:
                print("Try again.")
            self.chosenCards.clear()
        
    def incrementScoreVar(self):
        self.score += 1
        self.scoreVar.set(str(self.score))

class Deck:
    
    def __init__(self, parent):
        self.deckCards = [Card(parent,shape,color,shading,amount) \
         for shape in shapes for color in colors \
         for shading in shadings for amount in amounts] 
        random.shuffle(self.deckCards)
    
    def takeOne(self):
        if len(self.deckCards)>0:
            return self.deckCards.pop()
        else:
            return None

class Gamelogic:
    
    def shapeSet(self,card1,card2,card3):
        a = card1.shape == card2.shape
        b = card2.shape == card3.shape
        return (a and b) or (not a and not b)

    def colorSet(self,card1,card2,card3):
        a = card1.color == card2.color
        b = card2.color == card3.color
        return (a and b) or (not a and not b)

    def shadeSet(self,card1,card2,card3):
        a = card1.shading == card2.shading
        b = card2.shading == card3.shading
        return (a and b) or (not a and not b)

    def amountSet(self,card1,card2,card3):
        a = card1.amount == card2.amount
        b = card2.amount == card3.amount
        return (a and b) or (not a and not b)

    def isSet(self,threecards):
        return self.shapeSet(threecards[0],threecards[1],threecards[2]) and \
            self.colorSet(threecards[0],threecards[1],threecards[2]) and \
            self.shadeSet(threecards[0],threecards[1],threecards[2]) and \
            self.amountSet(threecards[0],threecards[1],threecards[2])

frameWidth = 800
frameHeight = 800
cardPadding=(20,20)

frame = Tk()
frame.title("SET")
frame.minsize(800,800)

allImages = []
deck = Deck(frame)
board = Board(frame)
board.initFillSlots()

for col in range(3):
    for row in range(4):
        board.getCardAt(col,row).grid(row=row,column=col,padx=cardPadding,pady=cardPadding)

frame.mainloop()

