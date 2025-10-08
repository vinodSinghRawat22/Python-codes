# 42. Write a program to count the number of words starting with a vowel in a string. 

string = input("Enter string: ").lower()

words = string.split()
vowels = 'aeiou'
count = 0
for word in words: 
    if word[0] in vowels:
        count +=1

print(f"The number of words starting with vowels are : {count}")