# x = "awesome"


def myFunc():
    global x
    x = "fantastic"
    print("Python is ", x)


myFunc()

print("Python is " + x)
