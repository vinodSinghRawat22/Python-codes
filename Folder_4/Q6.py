# 06. Write a script that checks if all characters in a string are digits.

string = input("Enter string : ")

digit = True
for i in string: 
    if i.isdigit():
        continue 
    else: 
        digit= False 
        break

if digit is True : 
    print ("String contain all the digits. ")
else:
    print ("String does not contain all the digits. ")