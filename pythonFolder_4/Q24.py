# 24. Write a program that accepts a sentence and calculates the number of upper and lower case letters. 

sentence = input("Enter a sentence: ")

upper = 0
lower = 0
for ch in sentence: 
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1

print(f"Number of upper case characters is : {upper}")
print(f"Number of lower case characters is : {lower}")