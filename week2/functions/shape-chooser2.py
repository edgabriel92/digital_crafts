from random import *
randomInsults = [
    "You serious?, it's either yes or no question ",
    "Dude come on, yes or no... ",
    "WTF, get your beep beep together!, yes or noooo ",
    "You mom.. yes or no: ",
    "You beep beep to the beep of beep... yes or beeping no?!",
    "Well then, try again... retard. yes or no..."
]
def paintShape():

    def randomInsult():
        randomOne = randint(0,5)
        return randomInsults[randomOne]

    def tryAgain(playAgain):
            if playAgain == "no":
                print "bye"
                return False
            elif playAgain == "yes":
                print "ok"  

    def shapeBuilder(num):
    
        if shape == 1:
            while True:
                try:
                     height = int(raw_input("What is the height? "))
                except ValueError:
                    print "Sorry, try again"
                    continue
                else:
                    break
            #create a triangle
            def createTriangle(height):
                for row in range(1, height + 1):
                    spaces = height - row    
                    print " " * spaces + "*" * (row * 2 - 1)
            createTriangle(height)
        elif shape is 2:
            while True:
                try:
                    side = int(raw_input("What is the side: "))
                except ValueError:
                    print "Sorry, try again"
                    continue
                else:
                    break
            #creating a square
            def createSquare(side):
                for x in range(5):
                    print "*" * 5
            createSquare(side)
        elif shape is 3:
            while True:
                try:
                    height = int(raw_input("What is the height? "))
                    width = int(raw_input("What is the width? "))
                except ValueError:
                    print "Sorry, try again"
                    continue
                else:
                    break
            #create a box
            def createBox(height, width):
                for row in range(height):
                    if row == 0 or row == height -1:
                        print "*" * width
                    else: 
                        spaces = width - 2
                        print "*" + " " * spaces + "*"
            createBox(height, width)
   
    while True:
        while True:
            try: 
                shape = int(raw_input("What shape do you wish to print?: \n 1 Triangle \n 2 Square \n 3 Box: "))
            except ValueError:
                print "That's not a shape mate. "
                continue
            else:
                break
        shapeBuilder(shape)
        #play again section
        playAgain = raw_input("Play again? yes/no: ")
        if tryAgain(playAgain) == False:
            return False
        while playAgain != ("yes" or "no"):
            playAgain = raw_input(randomInsult())
            if tryAgain(playAgain) == False:
                return False
                       
paintShape()