from turtle import *

def drawHexagon(size):
    for i in range(6):
        forward(size)
        left(60)

if __name__ == '__main__':
    drawHexagon() 
    mainlooop()   