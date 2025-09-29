# Q30. Write a program to display the cube of the number up to an integer.

num = int(input("Enter the integer you want to print cube:"))

if num > 0:
    for i in range (1, num+1):
        print(f"Cube of {i} = {i**3}")