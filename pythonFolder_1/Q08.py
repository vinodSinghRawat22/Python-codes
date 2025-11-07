# Q8. Create a program to count the number of vowels in a string. 

str = input ("Enter the String: ")
str = str.lower()
count = 0
for ch in str: 
    if ch == 'a' or ch == 'e' or ch =='i' or ch =='o' or ch == 'u' :
        count+=1

print(f"\nTotal no of vowels in String: ' {str}' are {count}\n")

