l = [11, 2, 3, 4, 5, 7]
print(l)

l.append(10)
print(l)

l.sort()
l.sort(reverse=True)
l.reverse()

m = l
m[0] = 110
print(m)
print(l)  # l also changes

m = l.copy()
m[0] = 1310

print(m)
print(l)

print(l.count(11))
print(l)

l.insert(2, 899)
print(l)

m = [900, 1000, 1100]
l.extend(m)  # important
print(l)

# concatenate two lists
# console.time("run")
k = l + m + l
print(k)
# console.timeEnd("run")
