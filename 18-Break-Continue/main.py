for i in range(13):
  print(i * i)

print("\n")

# Multiplication Table
for i in range(20):
  if (i == 4):  # skips when i == 4
    continue
  if (i >= 10):  # breaks the loop if i >= 10
    break
  print("5 X", i + 1, " = ", 5 * (i + 1))

# continue -> jumps to next iteration
# break    -> break the loop
