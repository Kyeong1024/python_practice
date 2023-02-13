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

        # same with upside
        # words[word] = words.get(word, 0) + 1

topFive = sorted([(v, k) for k, v in words.items()], reverse=True)[:5]
print("Top five:", topFive)

# same with topFive print
tmp = []
for k, v in words.items():
    tmp.append((v, k))

tmp = sorted(tmp, reverse=True)[:5]

for v, k in tmp:
    print(k, v)
