# 12. Create a program to check if a key exists in a dictionary. 

students = {'Vinod': "BCA", "Nandini": "MBBS", "Aayush" : "10th"}

name = input("Enter name to check: ").lower()

lst = [key.lower() for key in students.keys()]

if name in lst:
    print("Exist....")     
else: 
    print("Do not exist.")