bool("abc")
bool(123)
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myclass:
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))


def myFunction(x):
    if x & 1:
        return False
    else:
        return True


if myFunction(10):
    print("EVEN")
else:
    print("ODD")

x = 200
print(isinstance(x, int))
