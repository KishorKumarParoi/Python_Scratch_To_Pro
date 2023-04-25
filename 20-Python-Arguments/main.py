#def average(a=9, b=5, c = 1):
#print("The average is ", (a + b + c) / 2)


# tuple
def average(*numbers):
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  print("Average is: ", sum / len(numbers))


# 4 types of arguments we can provide

# average(10, 30)
# average(b=10, a=100)

average(3, 4, 52, 3, 2)

name = ["Amy", "Agarwal", "Jain"]
print(name)


def name(**name):
  print(type(name))
  print("Hello, ", name["fname"], name["mname"], name["lname"])


name(mname="Kumar", lname="Paroi", fname="Kishor")
# naame[mnasme="Kumar", lnasme="Paroi", fnasme="Kishor"]

