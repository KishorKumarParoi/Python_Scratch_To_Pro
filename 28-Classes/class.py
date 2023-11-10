class myClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
       return "Name: " + self.name + "\n" + "Age: " + self.age

    def func(self):
        print("Hello from a function")
        print("Hello " + self.name)

Kishor = myClass('Kishor', '24')
print(Kishor.name)
print(Kishor.age)
print(Kishor)
Kishor.func()

