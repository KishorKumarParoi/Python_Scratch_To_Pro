num = int(input("Enter Number : "))
if(num == 0):
   print("Zero")
elif(num > 0 and num < 101):
   if(num > 10 and num < 90):
       print("Num is greater than 10 but less than 90")
   elif (num >= 90 and num <= 100):
       print("Num lies between 90-100")
   else:
     print("Num is greater than Zero and less than 10")
else:
  print("Number is Negative")