name = "Kishor!! !!! Pallabi!!"
print(len(name))
print(name.upper())
print(name.lower())
print(name)
# Strings are immutable

# rstrip
print(name.rstrip("!"))  # Trailing Strip

# replace
print(name.replace("Kishor", "Pallabi"))

# split
print(name.split("!"))

# capitalize()
blogHeading = "introduction to jS"
print(blogHeading.capitalize())

# center()
str1 = "introduction to computer science"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))

# count
print(name.count("Kishor"))

# endsWith()
print(name.endswith("!!"))
print(name.endswith("shor", 1, 6))

str1 = "His name is Goverment Minister, etto is bacche thik"
print(str1.find("iss"))
print(str1.find("is"))
# print(str1.index("iss"))  #throws error
print(str1.index("Minister"))

name = "Kishor007"
print(name.isalnum())
print(name.isalpha())
print(name.islower())
print(name.isupper())
print(name.isprintable())

name = "Kishor007\n"
print(name.isprintable())
name = "   "
print(name.isspace())

name = "Kishor Kumar Paroi"
print(name.istitle())
print(name.startswith("K", 0, 10))
print(name.swapcase())
print(name.title())
