def computeSalary(hour, salary) :
  if (fh > 40):
      reg = hour * salary
      over = salary * (hour - 40) * 0.5
      pay = reg + over
  else:
      pay = salary * hour
  return pay

sr = input("Your salary: ")
sh = input("Work time: ")

try:
  fh = float(sh)
  fr = float(sr)
except:
  print("Input format must be numeric!")
  quit()


print("Total is", computeSalary(fh, fr))