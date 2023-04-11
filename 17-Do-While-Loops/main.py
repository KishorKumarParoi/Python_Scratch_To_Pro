# There is no builtin do-while loop in python yet we can emulate a do-while loop from while loop as per our necessity

secret_word = "python"
count = 0

while True:
  word = input("Enter Word : ").lower()
  count = count + 1
  if (word == secret_word):
    print("Ureeeeka!!! You got secret word")
    break
  else:
    if (count > 10):
      break
