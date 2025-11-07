# Q14. Check if a given year is a leap year or not.

year = int(input("Enter year : "))

if year % 4 == 0 and year % 100 != 0 :
    print( f"\n{year} is leap year")
    
elif year % 400 == 0 : 

    print (f"\n{year} is leap year.")
else: 
    print(f"\n{year} is not a leap year. ")