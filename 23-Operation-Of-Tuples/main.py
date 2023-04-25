countries = ("Spain", "Italy", "India", "England", "Germany")
tmp = list(countries)
print(tmp)
print(countries)
tmp.append("Bangladesh")
print(tmp)
tmp.pop(3)
print(tmp)
tmp[3] = "Canada"
countries = tuple(tmp)
print(countries)
print(tmp)

countries2 = ("Srilanka", "Russia", "USA")
print(countries + countries2)

tuple1 = (0, 1, 2, 3, 4, 4, 5, 55)
res = tuple1.count(4)
print(res)

res = tuple1.index(55)
print(res)

res = tuple1.index(3, 2, 5)
print(res)
print(len(tuple1))

tup = list(tuple1)
tup.append(2100)
tuple1 = tuple(tup)
print(tuple1)