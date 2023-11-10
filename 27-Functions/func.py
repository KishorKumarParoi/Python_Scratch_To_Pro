def my_func(*names):
    print("Hello from a function")
    print("Hello " + names[0])

my_func('Kishor', 'Rahim', 'Karim')

def my_func2(**names):
    print("Hello from a function")
    print("Hello " + names["age"])

my_func2(name = 'Kishor', age = '24', city = 'Dhaka')

