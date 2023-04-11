import time

# print(time.gmtime())
# print(time.time())

# print(time.ctime(time.time()))
# print(time.localtime(time.time()))
# print(time.mktime(time.localtime(time.time())))
# print(time.time())
# # print(time.gmtime())

# print(time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
# print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
# print(time.asctime(time.localtime()))

# print(time.strptime("Tue, 11 Apr 2023 08:41:41", "%a, %d %b %Y %H:%M:%S"))

# print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
# print(time.strftime("%-H", time.localtime()))

# n = "kishor"
# for x in n:
#   time.sleep(1)
#   print(x)

# print(time.time())
hour = int(time.strftime("%H", time.gmtime()))
hour += 6
print(hour)

if (hour == 6):
  print("Good Morning")
elif (hour == 12):
  print("Good Afternoon")
elif (hour == 18):
  print("Good Evening")
elif (hour == 0):
  print("Good Night")
else:
  print("Enjoy Happy Time")

timestamp = time.strftime("%H:%M:%S")
print(timestamp)