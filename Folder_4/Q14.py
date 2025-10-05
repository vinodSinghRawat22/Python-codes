# 14. Write a program that extracts all integers from a given text. 

text = input("Enter the text: ")

integers = []

for ch in text: 
    if ch.isdigit():
        integers.append (ch)
    else: 
        continue

if integers:
    print("Integers present in text are: ")
    for i in integers: 
        print(i, end = ' ')
else: 
    print("No integer present....")