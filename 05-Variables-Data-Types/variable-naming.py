"""
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""
# legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

# If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry", "komla"]
k, x, y, z = fruits
print(k)
print(x)
print(y)
print(z)

# Output Variables

print(k, x, y, z)
print(k + x + y + z)
print(k + " " + x + " " + y + " " + z)

x = 12
print(str(x) + y)  # error show korbe
