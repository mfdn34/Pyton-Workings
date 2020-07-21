year = input("Please enter a year : ")
while True:
    if year.isdigit() and int(year) > 0:
        year = int(year)
        break
    else:
        year = input("You entered incorrectly. Please enter a year : ")
  
if (year % 4) == 0:  
   if (year % 100) == 0:  
       if (year % 400) == 0:  
           print("{0} is a leap year".format(year))  
       else:  
           print("{0} is not a leap year".format(year))  
   else:  
       print("{0} is a leap year".format(year))  
else:  
   print("{0} is not a leap year".format(year)) 