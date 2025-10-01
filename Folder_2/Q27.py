# 27. Write a function to find the missing number from a list of 1 to N. 

import random

n = int(input("Enter the value of N : "))
numbers = list(range(1, n+1))
numbers.remove(random.choice(numbers))

print(f"List of numbers  from 1 to {n} : {numbers} ")


for i in range ( 1, n+1):
    if i in numbers: 
        continue
    else: 
        print(" The missing number is : ", i)         
    
