# 10. Write a script that finds all email addresses in a given text. 

text = input("Enter the text:")
words = text.split()
email_list = []

for word in words: 
    if "@" in word and '.' in word:
        email_list.append(word)
    else:
        continue
if not email_list:
    print("No email address found in text")
else:
    print("\n\n The email addresses present in text are :  ")
    for word in email_list:
        print(word)

# or by pre-defined function 

import re

emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)

if not emails:
    print("No email address found in text")
else:
    print("\n\n The email addresses present in text are :  ")
    for word in emails:
        print(word)
