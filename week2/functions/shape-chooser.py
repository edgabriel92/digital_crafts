import random

def ranInsult():
    insult = random.randint(1,3)
    if insult == 1:
        print "Okay lets try this again NumbSkull. Yes or No?"
    elif insult == 2:
        print "REALLY?! I asked Yes or No?"
    elif insult == 3:
        print "Error 10101001001010: I'm only as smart as the user. Yes or No"
    else:
        print "All hope in humanity lost due to your stupidity"

def triangle(height):
    base = height * 2 -1
    for row in range(1, height + 1):
        spaces = height - row
        print " " * spaces + "*" * (row * 2 - 1)
    print "Here you go!"

def square(length, width):
    print '*' * width
    num_spaces = width - 2
    spaces = ' ' * num_spaces
    for i in range(height - 2):
        print '*' + spaces + '*'
    print '*' * width
    print "Here you go!"

def box(width, height):
    for row in range(height):
        if row == 0:
            print '*' * width
        elif row == height - 1:
            print '*' * width
        else:
            spaces = width - 2
            print '*' + ' ' * spaces + '*'
    print "Here you go!"

def shapeMenu():
    shape = int(raw_input("What shape do you wish to print? \n1 Triangle \n2 Square \n3 Box \nChoose? "))
    if shape == 1: #triangle
        height = int(raw_input("How high? "))
        triangle(height)
    elif shape == 2: #square
        length = int(raw_input("How long? "))
        width = int(raw_input("How wide?" ))
        square(width, height)       
    elif shape == 3: #box
        height = int(raw_input("How high? "))
        width = int(raw_input("How wide? "))
        box(width, height)
    else:
        print "Please choose a number 1 - 3 to choose the corresponding shape."
        shapeMenu()
       
def playAgain():
    onceMore = raw_input("Play again? (yes/no) " ).lower()
    if onceMore == "yes":
        shapeMenu()
        playAgain()
    elif onceMore == "no":
        print "Bye!"
    else:
        ranInsult()
        playAgain()

shapeMenu()
playAgain()
    
