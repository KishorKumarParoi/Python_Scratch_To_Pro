def calculateGmean(a, b):
  mean = (a * b) / (a + b)
  print(mean)


# builtin function & user-defined function


def isGreater(a, b):
  if (a > b):
    print("first is greater")
  else:
    print("second number is greater or equal")


def isLesser(a, b):
  pass  # I will write latter this function


a = 9
b = 8
# gmean = (a * b) / (a + b)
c = 8
d = 432

isGreater(a, b)
calculateGmean(a, b)

isGreater(c, d)
calculateGmean(c, d)
