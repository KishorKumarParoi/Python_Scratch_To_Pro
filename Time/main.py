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
# print(hour)

name = input("Enter Your Name : ")

if (hour >= 0 and hour < 12):
  print("Good Morning", name)
elif (hour >= 12 and hour < 17):
  print("Good Afternoon", name)
elif (hour >= 17 and hour < 19):
  print("Good Evening", name)
elif (hour >= 19 and hour <= 23):
  print("Good Night", name)

# timestamp = time.strftime("%H:%M:%S")
# print(timestamp)
# timestamp = time.strftime("%H:%M:%S",time.localtime())
# prnit(timestamp)