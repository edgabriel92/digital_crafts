def word_histogram(sentence):
    tally = {}
    wordList = sentence.split()
    for word in wordList:
        if tally.get(word):
            tally[word] += 1
        else:
            tally[word] = 1
    return tally

# def top_three(tally):
#     top_three_items = {}
#     while len(top_three_items) < 3:
#         highkey = ''
#         highestValue = 0
#         for key, value in tally.items():
#             if value > highestValue:
#                 highkey = key
#                 highestValue = value
#         top_three_items[highkey] = [highkey]
#         del tally[highkey]
#     print top_three_items

def top_three(hist):
    sortedList = sorted(hist, key=hist.get)[::-1]

    print sortedList[0:3]

print top_three(word_histogram("happy happy joy joy happy man"))