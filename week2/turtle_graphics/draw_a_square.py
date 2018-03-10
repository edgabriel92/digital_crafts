from turtle import *


def drawSquare(size):
    for i in range(4):
        forward(size)
        left(90)

if __name__ == '__main__':
    drawSquare()

    up()
    forward(200)
    down()

    drawSquare()

    mainloop()
