
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100==0 :
    if year % 400==0:
      print("Leap year.")
    else:
      print("Not leap year.")  
  else:
    print("Leap year.") 
else:
  print("Not leap year.")

#Algo -> Refer : https://www.timeanddate.com/date/leapyear.html#:~:text=Leap%20Year%20Rules%3A%20How%20to%20Calculate%20Leap%20Years,by%20100%2C%20it%20is%20not%20a%20leap%20year

"""
In the Gregorian calendar, three criteria must be taken into account to identify leap years:

The year must be evenly divisible by 4;
If the year can also be evenly divided by 100, it is not a leap year;
"unless..."
The year is also evenly divisible by 400. Then it is a leap year.

"""