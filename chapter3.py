sr = input("Your salary: ")
sh = input("Work time: ")

try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Input format must be numeric!")
    quit()

if (fh > 40):
    reg = fr * fh
    over = fr * (fh - 40) * 0.5
    xp = reg + over
else:
    xp = fr * fh

print("Total is", xp)