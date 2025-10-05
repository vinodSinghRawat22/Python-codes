# 18. Write a Python program to read a file and display all lines that contain a given keyword. 

with open("file18.txt", 'r') as file: 
    lines = file.readlines()

keyword = input("Enter the keyword: ")

for i in range (0, len(lines)):
    if keyword.lower() in lines[i].lower(): 
        print(f"Keyword present in line {i+1} which is : {lines[i]}")