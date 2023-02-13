fhand = open("mbox-short.txt")

for str in fhand:
    str = str.rstrip()
    if (str == ""): continue

    splited = str.split()

    if (len(splited) < 3 or splited[0] != "From"): 
       continue
    print(str)
