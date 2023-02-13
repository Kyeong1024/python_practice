fname = input("Write file name with ext: ")
try:
    fhand = open(fname)
except:
    print("Wrong file name!")
    quit()

count = 0
for str in fhand:
    str = str.rstrip()
    print(str.upper())
    count = count + 1

print("count:", count)