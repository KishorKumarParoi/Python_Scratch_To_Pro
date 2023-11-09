fruits = ['Banana', 'Apple', 'kiwi', 'orange', 'Mango', 'Peach']
fruits = tuple(fruits)
print(fruits)

x = ('apple',)
print(type(x))
print(x)

print(len(x))

x = tuple(('apple', 'banana', 'cherry'))
print(x)

print(fruits[-4:-1])

fruits = list(fruits)
fruits[1] = 'Pineapple'
fruits = tuple(fruits)
print(fruits)

# unpacking tuple

(kkp, *kk, pk) = fruits
print(kkp)
print(kk)
print(pk)

fruits += x;
print(fruits)

fruits = fruits * 2
print(fruits)

print(fruits.count('apple'))
print(fruits.index('apple'))
