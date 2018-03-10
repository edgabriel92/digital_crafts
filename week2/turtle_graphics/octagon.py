from turtle import *

def drawOctagon(size):
    for i in range(8):
        forward(size)
        left(45)

if __name__ == '__main__':
    drawOctagon()
    mainloop()


