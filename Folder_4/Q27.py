# 27. Create a Python function to check if a string is a pangram(contain all latter from a-z).

string = input("Enter a string: ").lower()
characters = 'abcdefghijklmnopqrstuvwxyz'

pangram = True
for i in range(26):
    if characters[i] not in string: 
        pangram = False

if pangram is True: 
    print("Yes! string is pangram")
else: 
    print("No! string is not pangram ")