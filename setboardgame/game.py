import itertools as it
from tkinter import *
import random
from PIL import Image as Img, ImageTk as ImgTk
import os

dirname = os.path.dirname(__file__)

# diamond, oval and squiggle
shapes = ["diamond","oval","squiggle"]

colors = ["red","green","purple"]

# solid striped outlined
shadings = ["full","striped","empty"]

amounts = [1,2,3]

class Card:
    
    def __init__(self,shape,color,shading,amount):
        self.shape = shape
        self.color = color
        self.shading = shading
        self.amount = amount

class Board:
    
    chosenCardNext = 0
    
    def __init__(self):
        self.cardSlots = [[None,None,None],\
                          [None,None,None],\
                          [None,None,None],\
                          [None,None,None]]
        self.chosenCards = []
        self.chosenCardsX = []
        self.chosenCardsY = []
    
    def setCard(self,posX,posY,card):
        self.cardSlots[posY][posX] = card
    
    def getCard(self,posX,posY):
        return self.cardSlots[posY][posX]

    def chooseCard(self,posX,posY):
        self.chosenCards.append(self.cardSlots[posY][posX])
        self.chosenCardsX.append(posX)
        self.chosenCardsY.append(posY)
        Board.chosenCardNext += 1
        if Board.chosenCardNext == 3:
            if self.chosenCardsInSet():
                print("That's a set!")
                for x,y in zip(self.chosenCardsX,self.chosenCardsY):
                    newCardAt(x,y)
                self.clearChosenCards()
            else:
                print("Try again.")
                self.clearChosenCards()
            Board.chosenCardNext = 0
    
    def chosenCardsInSet(self):
        return isSet(self.chosenCards)
    
    def clearChosenCards(self):
        self.chosenCards = []
        self.chosenCardsX = []
        self.chosenCardsY = []

    def initFillSlots(self,deck):
        for i in range(3):
            for j in range(4):
                self.setCard(i,j,deck.takeOne())
        return deck

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

def drawCard(card,posX,posY):
    if cardRefs[posY][posX]:
        for shape in cardRefs[posY][posX]:
            canvas.delete(shape)
    cardx = cardX(posX)
    cardy = cardY(posY)
    canvas.create_rectangle(cardx, cardy,\
                            cardx+cardwidth, cardy+cardheight, tags = str(posX)+" "+str(posY), activefill = "grey")
    shapes = drawCardImage(card,cardx,cardy)
    cardRefs[posY][posX] = shapes

def drawCardImage(card,x,y):
    return drawShapes(x,y,card.amount,card.shape,card.color,card.shading)
        

def drawShapes(x,y,amount,shape,color,shading):
    paddingX = (cardwidth-shapeWidth)//2
    paddingY = (cardheight-shapeHeight)//2
    distBetween = 10
    correction = 0
    shapes = []
    if amount == 2:
        correction -= (shapeWidth+distBetween)/2
    elif amount == 3:
        correction -= shapeWidth+distBetween
    for _ in range(amount):
        shapes.append(drawShape(paddingX + x + correction,paddingY + y,shapeWidth,shapeHeight,shape,color,shading))
        correction += shapeWidth+distBetween
    return shapes

def drawShape(x,y,w,h,shape,color,shading):
    img = Img.open(os.path.join(dirname, 'resources/'+shape+color+shading+'.png'))
    img = img.resize((w, h), Img.ANTIALIAS)
    tk_img = ImgTk.PhotoImage(img)
    imgs.append(tk_img)
    return canvas.create_image(x, y, image=tk_img, anchor='nw')

def cardX(X):
    return leftmargin + X*cardwidth + X*cardHorisontalMargin

def cardY(Y):
    return topmargin + Y*cardheight + Y*cardVerticalMargin

def click(event):
    if canvas.find_withtag(CURRENT):
        tags = canvas.gettags(CURRENT)
        slotX = int(tags[0])
        slotY = int(tags[1])
        board.chooseCard(slotX,slotY)

def newCardAt(x,y):
    board.setCard(x,y,deck.takeOne())
    drawCard(board.getCard(x,y),x,y)

def drawFirstCards():
    for i in range(3):
        for j in range(4):
            drawCard(board.getCard(i,j),i,j)

frame = Tk()
frame.title("SET")
imgs = []
cardwidth = 200
cardheight = 130
shapeWidth = 30
shapeHeight = 60
topmargin = 50
leftmargin = 50
cardVerticalMargin = 20
cardHorisontalMargin = 20
canvas = Canvas(frame, width=800, height=800, background="white")
canvas.grid()

deck = Deck()
board = Board()
deck = board.initFillSlots(deck)
cardRefs = [[None,None,None],\
            [None,None,None],\
            [None,None,None],\
            [None,None,None]]
drawFirstCards()

canvas.bind("<Button-1>", click)

frame.mainloop()

