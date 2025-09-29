# Q29. Create a program to check whether a number is prime or not.

num = int(input("Enter the number : "))

for i in (2,num+1):
    if num % i== 0: 
        if num == i:
            print(f"{num} is a prime number.")
            break      
else: 
    print(f"{num} is not a prime number. ")