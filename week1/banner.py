userText = raw_input("Text? ")
space = len(userText)

for row in range(space):
    if row == 0:
        print '*' * space
    elif row - 1 == space:
        print '*' * space