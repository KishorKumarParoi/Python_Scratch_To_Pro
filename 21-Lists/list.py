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
