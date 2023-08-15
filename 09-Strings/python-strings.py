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

x = 100
txt = "The temperature is {} degrees"
print(txt.format(x))

apple = 100
komla = 20
jam = 10

order = "I order {} apples, {} komla and {} jam"
print(order.format(apple, komla, jam))

order = "I order {2} apples, {0} komla and {1} jam"
print(order.format(apple, komla, jam))

order = "I order {c} apples, {b} komla and {a} jam"
print(order.format(a=apple, b=komla, c=jam))
