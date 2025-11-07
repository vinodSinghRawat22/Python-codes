# 21. Write a Python program to check if a string has all unique characters. 

string = input ("Enter a string: ")

if len(string) == len(set(string)) : 
    print("All characters in the string. ")
else :
    print("There are duplicate characters in the string. ")