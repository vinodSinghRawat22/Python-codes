# 09. Write a program to parse a date string and display it in a different format. 
from datetime import datetime

date = input("Enter the date (DD-MM-YYYY): ")

dateObject = datetime.strptime(date , "%d-%m-%Y")


formatted_date1 = dateObject.strftime("%B %d, %Y") 
formatted_date2 = dateObject.strftime("%d/%m/%Y")    

print(f"Original date : {date}")
print(f"Formatted date 1 : {formatted_date1}")
print(f"Formatted date 2 : {formatted_date2}")