# word = 'cheese' 
word = raw_input('sentence: ')
long_vowels = ['oo', 'ee', 'ii', 'aa', 'uu']

result = ''

for index in range(len(word)):
    twoletters = word[index:index+2]
    if twoletters in long_vowels:
        result += word[index] * 4
    else:
        result += word[index]

print result
"""
word = word.replace('aa', 'aaaaa')
word = word.replace('ee', 'eeeee')
word = word.replace('ii', 'iiiii')
word = word.replace('oo', 'ooooo')
word = word.replace('uu', 'uuuuu')
"""