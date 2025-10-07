# 34. Write a script to convert a string into title case without using .title(). 

string = input("Enter a string: ")

words = string.split()
modified_string = ""
for word in words: 
    modified_string += word[0].upper()+ word[1:].lower()+ " "

print(f"Modified string: {modified_string.strip()}")
