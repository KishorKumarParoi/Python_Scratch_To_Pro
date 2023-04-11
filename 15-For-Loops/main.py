name = "Kishor"
print(name)

cnt = 0
for i in name:
  if (cnt < len(name) - 1):
    print(i, end=",")
  else:
    print(i)
  cnt += 1

colors = ["red", 'green', 'blue', 'yellow']
for color in colors:
  print(color)
  for i in color:
    print(i)

for k in range(5):
  print(k + 1, end=" ")
print("\n")

for k in range(5, 9):
  print(k, end=" ")
print("\n")

for k in range(1, 10, 3):
  print(k)
