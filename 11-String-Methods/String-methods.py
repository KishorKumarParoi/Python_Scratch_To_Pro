# String Methods

# 1. capitalize
# 2. casefold
# 3. center
# 4. count
# 5. encode
# 6. endswith
# 7. expandtabs
# 8. find
# 9. format
# 10. format_map
# 11. index
# 12. isalnum
# 13. isalpha
# 14. isascii
# 15. isdecimal
# 16. isdigit
# 17. isidentifier
# 18. islower
# 19. isnumeric
# 20. isprintable
# 21. isspace
# 22. istitle
# 23. isupper
# 24. join
# 25. ljust
# 26. lower
# 27. lstrip
# 28. maketrans
# 29. partition
# 30. replace
# 31. rfind
# 32. rindex
# 33. rjust
# 34. rpartition
# 35. rsplit
# 36. rstrip
# 37. split
# 38. splitlines
# 39. startswith
# 40. strip
# 41. swapcase
# 42. title
# 43. translate
# 44. upper
# 45. zfill

txt = "hello, and welcome to my world."
txt.capitalize()
print(txt)

txt = "Hello, And WeLcome To My World."
txt.casefold()
print(txt)

txt = "banana"
txt.center(20)
print(txt)

txt = "I love apples, apple are my favorite fruit"
txt.count("apple")
print(txt)

txt = "My name is Ståle"
txt.encode()
print(txt)

txt = "Hello, welcome to my world."
print(txt.endswith("."))
print(txt.endswith("my world.", 5, 11))

txt = "H\te\tl\tl\to"
txt.expandtabs(2)
print(txt)

txt = "Hello, welcome to my world."
print(txt.find("welcome"))
print(txt.index("welcome"))
print(txt.find("e", 5, 10))

# named indexes:
txt1 = "My name is {fname}, I'm {age}, I got salaray {salary:.2f}".format(
    fname="John", age=36, salary=120
)
# numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John", 36)
# empty placeholders:
txt3 = "My name is {}, I'm {}".format("John", 36)

print(txt1)
print(txt2)
print(txt3)

# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))

txt = "Company420"
print(txt.isalnum())

txt = "CompanyX"
print(txt.isalpha())

txt = "Company123"
print(txt.isalnum())

txt = "\u0047"  # unicode for G
x = txt.isdecimal()
print(x)

txt = "50800"
x = txt.isdigit()
print(x)

txt = "Demo"
x = txt.isidentifier()
print(x)

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

txt = "hello world!"
x = txt.islower()
print(x)

txt = "565543"
x = txt.isnumeric()
print(x)

txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

txt = "   "
x = txt.isspace()
print(x)

txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

txt = "banana"
x = txt.rjust(20)

print(x, "is my favorite fruit.")

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

txt = "Welcome to my world"
x = txt.title()
print(x)

txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

txt = "Hello my friends"
x = txt.upper()
print(x)

txt = "50"
x = txt.zfill(10)
print(x)
