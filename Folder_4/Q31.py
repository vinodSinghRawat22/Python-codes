# 31. Create a program that extracts numbers from a string and returns their sum. 

string = input("Enter a string: ")

sum = 0 
for ch in string:
    if ch.isdigit():
        sum += int(ch)
print(sum)