# Q4. Create a program that prints the multiplication table of a given number

num = int( input(" Enter the number:"))

print (f'Table of {num} is : ')
for i in range (1, 11): 
    print (f"{num} * {i}  = {num * i}")