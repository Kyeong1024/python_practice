name = input("File name:")
try:
    rfile = open(name)
except:
    print("Wrong file name!")
    quit()
words = dict()

for str in rfile:
    str = str.rstrip()
    splited = str.split()

    if (len(splited) == 0): continue
    for word in splited:
        if (word in words):
            words[word] += 1
        else: 
            words[word] = 1
        # words[word] = words.get(word, 0) + 1

mostBigWord = None
mostBigCount = 0

for word, count in words.items():
    if (mostBigWord is None and mostBigCount == 0):
        mostBigWord = word
        mostBigCount = count
    
    if (count > mostBigCount):
        mostBigWord = word
        mostBigCount = count

print("MostBigWord:", mostBigWord, "MostBigCount:", mostBigCount)