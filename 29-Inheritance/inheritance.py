class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("Name: " + self.name + "\n" + "Age: " + str(self.age))


class Student(Person):
    # pass
    def __init__(self, name, age , city):
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self.city = city
    
    def info(self):
        print("Name: " + self.name + "\n" + "Age: " + str(self.age) + "\n" + "City: " + self.city)


x = Student("Kishor", 24, 'Dhaka')
print(x.name)
x.print_info()
print(x.city)
x.info()