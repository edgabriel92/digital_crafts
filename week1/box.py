width = int(raw_input("Width? "))
height = int(raw_input("Height? "))

for row in range(height):
    if row == 0:
        print '* ' * width
    elif row - 1 == height:
        print '*' * width
        

