x = list(("apple", "komla", "lebu"))
print(x)

y = ["aam", "jam", "lichu"]
print(y)

z = x + y * 2
print(z)

print(z[0])
print(z[1])
print(z[2:5])
print(z[-1])
print(z[:4])
print(z[2:])

if "apple" in z:
    print("Yes")

print(len(z))
z[1] = "kathal"
z[3:6] = ["blackpink", "jambura"]
print(z)
z.insert(2, "kola")
print(z)

z.append("Shalar Put")
print(z)

z.remove("kola")
print(z)

z.extend(["kola", "kathal"])
print(z)
z.extend(y)
print(z)
z.pop()
print(z)

thistuple = ("apple", "banana", "cherry")
z.append(thistuple)
print(z)
z.extend(thistuple)
print(z)

z.pop(2)
print(z)
z.remove("kathal")
print(z)
del z[3]
print(z)
y = z
print(y)
# z.clear()
# print(z)
# del z
# print(z)  # error

for x in z:
    print(x)

for i in range(len(z)):
    print(z[i])

i = 0
while i < len(z):
    print(z[i])
    i += 1

#  shortest text

[print(x) for x in z]

newlist = []
for x in z:
    if "a" in x:
        newlist.append(x)
print(newlist)

newlist = [x for x in z if "a" in x]
print(newlist)

newlist = [x for x in z if x != "kola"]
print(newlist)

z.pop(-4)
z.sort()
print(z)

z.sort(reverse=True)
print(z)

numbers = [10, 1, 23, 233, 3, 7, 9, 100]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)


def myfunc(n):
    return abs(n - 50)


numbers.append(49)
numbers.sort(key=myfunc)
print(numbers)

z.sort(key=str.lower)
print(z)

z.reverse()
print(z)
