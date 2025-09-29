# Q23. Write a Python program to print a pattern of stars in a triangle. 

rows = int(input("Enter the number of rows you want in triangle: "))

print("\nTringle 1 : ")
for i in range (1, rows+1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

print("\nTringle 2 : ")

for i in range (1, rows+1):
    print("*"*i)

print("\nTringle 3:")

for i in range (rows,0 , -1):
    print("*"*i)