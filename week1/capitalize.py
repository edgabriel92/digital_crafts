stringToReverse = raw_input("Reverse this: ")

wordLength = len(stringToReverse)

reveserdWord = ''

for char in range(wordLength):
    print stringToReverse[(wordLength - 1) - char]

print "reversed word: %s" % reversedWord