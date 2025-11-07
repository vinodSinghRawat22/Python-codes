# Q17. Write a program to find the LCM of two numbers. 

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
a , b = num1 ,num2

while b != 0:
    temp = b
    b = a % b 
    a = temp
   
gcd= a 

lcm = (num1 * num2)// gcd

print(f"\nLCM of {num1} and {num2} is : {lcm}")

# or.............

import math 

print(f"\nLCM of {num1} and {num2} is : {math.lcm(num1,num2)}")
