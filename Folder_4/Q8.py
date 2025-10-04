# 08. Create a function that removes all HTML tags from a string.

text = input("Enter the string which contain HTML tags : ")
result = ""
inside = False
for ch in text:
    if ch == '<':
        inside = True
    elif ch == '>':
        inside = False
    elif not inside:
        result += ch

print(f"Original text : {text}")
print(f"After removing HTML tags : {result}")


# By using function 

import re

text = input("Enter the string which contain HTML tags : ")

new_text = re.sub('<[^<]+?>', '', text)

print(f"Original text : {text}")
print(f"After removing HTML tags : {new_text}")


