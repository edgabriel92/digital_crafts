def triangle(height):
    base = height * 2 -1
    for row in range(1, height + 1):
        spaces = height - row
        print " " * spaces + "*" * (row * 2 - 1)

def square(width, height):
    print '*' * width
    num_spaces = width - 2
    spaces = ' ' * num_spaces
    for i in range(height - 2):
        print '*' + spaces + '*'
    print '*' * width

def box(width, height):
    for row in range(height):
        if row == 0:
            print '*' * width
        elif row == height - 1:
            print '*' * width
        else:
            spaces = width - 2
            print '*' + ' ' * spaces + '*'

shape = int(raw_input("What shape do you wish to print? \n1 Triangle \n2 Square \n3 Box \nChoose? "))

if shape == 1:
    height = int(raw_input("How high? "))
    triangle(height)
    print "Bye!"
elif shape == 2:
    length = int(raw_input("How long? "))
    width = int(raw_input("How wide?" ))
elif shape == 3:
    height = int(raw_input("How high? "))
    width = int(raw_input("How wide? "))
else:
    print "Please choose a number 1 - 3."
