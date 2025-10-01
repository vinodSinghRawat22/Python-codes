# 15. Write a function that returns the factorial of a number. 

def factorial(n): 
    if n == 0 : 
       return 1
    else: 
       return n*factorial(n-1)

num = int(input("Enter the number: "))
print(f"factorial of {num} is : {factorial(num)}")