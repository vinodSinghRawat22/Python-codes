# Q5. Write a program to find the largest of three numbers.

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if (num1>num2) and (num1 >num3):
    print (f"The greatest number is: {num1}")

elif(num2 > num1) and (num2 > num3):
    print (f"The greatest number is: {num2}")

elif(num3 > num1) and (num3 > num1):
    print (f"The greatest number is: {num3}")

else:
    print (f"All numbers are equal.")
