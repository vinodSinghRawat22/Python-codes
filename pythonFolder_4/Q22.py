# 22. Create a program that removes all duplicate characters from a string. 

string = input("Enter a string: ")

unique = ""

for ch in string: 
    if ch not in unique :
        unique +=ch 
    
print(f" The string after removing duplicate characters :  {unique}")