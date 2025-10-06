# 29. Write a program to check if two strings are anagrams. 

string1 = input("Enter first string: ").lower().replace(" ", "")
string2 = input("Enter second string: ").lower().replace(" ", "")


if len(string1) == len(string2):    
    if sorted(string1) == sorted(string2): 
        print("Strings are anagrams")
    else: 
        print("Strings are not anagrams")
else: 
    print("Strings are not anagrams")