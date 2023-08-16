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
