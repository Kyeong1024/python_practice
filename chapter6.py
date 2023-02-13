# String parsing practice
str = "X-DSPAM-Confidence: 0.8475 "
start = str.find(":")
target = float(str[start + 1 :].strip())
print(target)
str[7] = "!"
print(str)
# String practice
# data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2023"
# start = data.find("@")
# end = data.find(" ", start)

# location = data[start + 1: end]
# print(location)

