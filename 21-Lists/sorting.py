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


def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)

def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)
print(cars)