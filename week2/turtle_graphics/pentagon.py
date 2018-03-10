from turtle import *

def drawPentagon(size):
    for i in range(5):
        forward(size)
        left(72)


if __name__ == '__main__:
    drawPentagon()
    mainloop()


