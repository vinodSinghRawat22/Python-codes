# 40. Write a program that accepts a string and counts vowels and consonants. 

string = input("Enter the string: ").lower()

vowels= "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
vowels_count = 0
consonants_count = 0
for ch in string:
    if ch in vowels: 
        vowels_count+=1
    elif ch in consonants: 
        consonants_count+= 1

print ("Number of vowels ", vowels_count)
print ("Number of consonants: ", consonants_count)
