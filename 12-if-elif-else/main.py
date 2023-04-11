# 2 Days Mission
age = int(input("Enter Your Age : "))
print("Your Age is : ", age)

# conditional operator -> >, <, >=, <=, ==, !=

if (age > 18 and age < 100):
  print("Yes")
  print("You can drive")
elif (age >= 6 and age <= 18):
  print("No")
  print("You can't drive")
elif (age >= 100):
  print("Grandfather")
  print("You better beware of breaking bone")
else:
  print("You better play with toy")
print("Yayy")   # Indentation is key factor for blocking