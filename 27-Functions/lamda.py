square = lambda x : x * x
cube = lambda x : x * x * x

def my_func(x):
    print("Hello from a function")
    print(square(x))
    return cube(x)

print(my_func(10))

