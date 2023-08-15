a = "Helxo World"
print(a[1:4])
print(a[1:])
print(a[:4])
print(a[-5:-2])
print(a[-5:])
print(a[:-2])
print(a[-2:])
print(a[1:-2])
# print(a[1:-2:2])
# print(a[1:-2:3])

for x in "banana":
    print(x)

print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print("Yes, 'free' is present.")

if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")


# String methods
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "K"))

print(a.split(","))  # returns ['Hello', ' World!']
