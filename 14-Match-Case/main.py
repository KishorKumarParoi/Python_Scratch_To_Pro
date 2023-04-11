import os

print("Hello World")
os.system("python --version")

# Match Case 
x = int(input("Enter the value of x : "))
match x:
     case 0:
       print("x is zero")
     case 4:
       print("case is 4")
     case _ if x == 80:
       print("Value is : ", x)
     case _ if x != 90:
       print(x, "isnot 90")
     case _:
       print("value is : ", x)