numbers = [2, 7, 4, -5, 1, 6,]
factor = 3
newArray = []

for number in numbers:    
    newNum = number * factor 
    newArray.extend([newNum])
print newArray
 