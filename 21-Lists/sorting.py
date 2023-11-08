numbers = [1, 3, 4, 2, -20, 100]
fruits = ['Banana', 'Apple', 'kiwi', 'orange', 'Mango', 'Peach']

# sort() method
numbers.sort() # numerical order
print(numbers)
fruits.sort()   # alphabetical order
print(fruits)

numbers.sort(reverse=True) # reverse numerical order
print(numbers)
fruits.sort(reverse=True)  # reverse alphabetical order
print(fruits)

# sorted() function

def myFunc(n):
    return abs(n-50)

numbers.sort(key = myFunc)
print(numbers)

numbers.sort(key = lambda n: abs(n-50))
print(numbers)

fruits.sort(key = str.lower)
print(fruits)