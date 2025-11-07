# Q7. Write a program to calculate the factorial of a number using a loop.

num = int(input("Enter the number: "))

fact = 1

for i in range (num , 1, -1):
      fact= fact * i

print(f"Factorial of {num} is {fact}")