# Q16. Write a program to find the GCD of two numbers.

num1 = int(input("Enter 1st number : "))

num2 = int(input("Enter 2nd number : "))

a , b = num1 ,num2

while b != 0:
    temp = b
    b = a % b 
    a = temp

print(f"GDC of {num1} and {num2} is : {a}")