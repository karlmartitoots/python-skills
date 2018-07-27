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

class Card:
    
    def __init__(self,shape,color,shading,amount):
        self.containerWidth, self.containerHeight = 200,130
        self.shapeWidth, self.shapeHeight = 30,60
        self.distBetweenShapes = 10
        self.shape = shape
        self.color = color
        self.shading = shading
        self.amount = amount
        self.shapeImage = self.loadImage()
        self.containerObject = None
        self.shapeObjects = []
    
    def loadImage(self):
        cardImage = Img.open(os.path.join(dirname, 'resources/'+self.shape+self.color+self.shading+'.png'))
        resizedCardImage = cardImage.resize((self.shapeWidth, self.shapeHeight), Img.ANTIALIAS)
        tkCardImage = ImgTk.PhotoImage(resizedCardImage)
        allImages.append(tkCardImage)
        return tkCardImage
    
    def drawShapesInContainer(self,leCanvas,containerTopX,containerTopY):
        horistontalPadding = (self.containerWidth-self.shapeWidth)/2
        verticalPadding = (self.containerHeight-self.shapeHeight)/2
        horisontalCorrection = 0
        if self.amount == 2:
            horisontalCorrection -= (self.shapeWidth+self.distBetweenShapes)/2
        elif self.amount == 3:
            horisontalCorrection -= self.shapeWidth+self.distBetweenShapes
        for _ in range(self.amount):
            self.shapeObjects.append(leCanvas.create_image(horistontalPadding + containerTopX + horisontalCorrection, verticalPadding + containerTopY, image=self.shapeImage, anchor='nw'))
            horisontalCorrection += self.shapeWidth+self.distBetweenShapes
        
    def drawContainerAt(self,leCanvas,topX,topY,col,row):
        self.containerObject = leCanvas.create_rectangle(topX, topY,\
                            topX+self.containerWidth, topY+self.containerHeight, tags = str(col)+" "+str(row))

    def drawAt(self,leCanvas,topX,topY,col,row):
        self.drawContainerAt(leCanvas,topX,topY,col,row)
        self.drawShapesInContainer(leCanvas,topX,topY)

class Board:
    
    chosenCardCount = 0
    
    def __init__(self, gameCanvas):
        self.cardSlots = [[None,None,None],\
                          [None,None,None],\
                          [None,None,None],\
                          [None,None,None]]
        self.chosenCards = []
        self.deck = Deck()
        self.gameCanvas = gameCanvas
        self.boardLeftMargin,self.boardTopMargin = 50,50
        self.distBetweenCardsX, self.distBetweenCardsY = 20, 20
    
    def setCardAt(self,col,row,card):
        self.cardSlots[row][col] = card
    
    def getCardAt(self,col,row):
        return self.cardSlots[row][col]

    def chooseCard(self,posX,posY):
        self.chosenCards.append(self.cardSlots[posY][posX])
        Board.chosenCardCount += 1
        if Board.chosenCardCount == 3:
            if self.chosenCardsInSet():
                print("That's a set!")
                for chosenCard in self.chosenCards:
                    coords = self.gameCanvas.gettags(chosenCard.containerObject).split(" ")
                    self.replaceCardAt(coords[0],coords[1],self.deck.takeOne())
            else:
                print("Try again.")
            self.chosenCards = []    
            Board.chosenCardCount = 0
    
    def chosenCardsInSet(self):
        return isSet(self.chosenCards)

    def initFillSlots(self):
        for col in range(3):
            for row in range(4):
                self.setCardAt(col,row,self.deck.takeOne())
    
    def initDrawBoard(self):
        for col in range(3):
            for row in range(4):
                nextCard = self.getCardAt(col,row)
                cardTopX = self.boardLeftMargin + col*nextCard.containerWidth + col*self.distBetweenCardsX
                cardTopY = self.boardTopMargin + row*nextCard.containerHeight + row*self.distBetweenCardsY
                nextCard.drawAt(self.gameCanvas,cardTopX,cardTopY,col,row)
    
    def replaceCardAt(self,col,row,newCard):
        cardAtRemoval = self.getCardAt(col,row)
        self.gameCanvas.delete(cardAtRemoval.containerObject)
        self.gameCanvas.delete(cardAtRemoval.shapeObjects)
        self.setCardAt(col,row,newCard)

class Deck:
    
    def __init__(self):
        self.deckCards = [Card(shape,color,shading,amount) \
         for shape in shapes for color in colors \
         for shading in shadings for amount in amounts] 
        random.shuffle(self.deckCards)
    
    def takeOne(self):
        return self.deckCards.pop()

def shapeSet(card1,card2,card3):
    a = card1.shape == card2.shape
    b = card2.shape == card3.shape
    return (a and b) or (not a and not b)

def colorSet(card1,card2,card3):
    a = card1.color == card2.color
    b = card2.color == card3.color
    return (a and b) or (not a and not b)

def shadeSet(card1,card2,card3):
    a = card1.shading == card2.shading
    b = card2.shading == card3.shading
    return (a and b) or (not a and not b)

def amountSet(card1,card2,card3):
    a = card1.amount == card2.amount
    b = card2.amount == card3.amount
    return (a and b) or (not a and not b)

def isSet(threecards):
    return shapeSet(threecards[0],threecards[1],threecards[2]) and \
           colorSet(threecards[0],threecards[1],threecards[2]) and \
           shadeSet(threecards[0],threecards[1],threecards[2]) and \
           amountSet(threecards[0],threecards[1],threecards[2])

def click(event):
    if canvas.find_withtag(CURRENT):
        print(canvas.gettags(event.widget.find_withtag(CURRENT)))
        tags = canvas.gettags(CURRENT)
        #slotX = int(tags[0])
        #slotY = int(tags[1])
        #board.chooseCard(slotX,slotY)

frame = Tk()
frame.title("SET")
canvas = Canvas(frame, width=800, height=800, background="white")
canvas.grid()
allImages = []

deck = Deck()
board = Board(canvas)
board.initFillSlots()
board.initDrawBoard()

canvas.bind("<Button-1>", click)

frame.mainloop()

