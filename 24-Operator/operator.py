"""
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators

"""
# identity operators
x = ["apple", "komla"]
y = ["apple", "komla"]
z = x

print(x is y)
print(x == y)

print(x is z)
print(x == z)

print(y is z)
print(y == z)

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# membership operators
x = ["apple", "banana"]
print("apple" in x)
print("banan" is not x)
