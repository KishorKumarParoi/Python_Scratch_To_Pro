# let's learn tuples

tup = (1, 24, 2, 4, 5, "Kishor", "Green")  # comma is necessary
print(type(tup), tup)

# tup[0] = 99  # tuple value can't be changed

# tuple = [1, 2, 3, 4, 44]
# print(type(tuple))
# print(tuple)

# tuple is used for const
print(len(tup), tup[-5])

if 342 in tup:
  print("Yes")
else:
  print("No")

# new tuple returns after slicing

tup2 = tup
# tup2.append(10)
print(tup)
print(tup2[1:-4])