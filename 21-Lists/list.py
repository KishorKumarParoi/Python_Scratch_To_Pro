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
