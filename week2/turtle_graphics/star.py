from turtle import *

def drawStar(size):
    for i in range(5):
        forward(size)
        right(144)
        forward(size)
        right(72-144)
    

if __name__ == '__main__':
    drawStar()
    mainloop()