numbers = [2, 7, 4, -5, 1, 6,]
evenNum = 0

for number in numbers:
    evenNum = number % 2    
    if evenNum == 0:
        evenNum = number
        print evenNum
 