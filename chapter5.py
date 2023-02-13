number = 0
sum = 0
count = 0

while True:
    number = input("Enter number: ")
    if (number == "done"): 
        break
    try:
        integer = float(number)
    except:
        print("please write numeric!")
        continue
    sum = sum + integer
    count = count + 1

print("sum:", sum, "count:", count, "avg:", sum / count)