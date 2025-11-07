# 11. Write a program to sort a list in ascending order. 

a = int(input("Enter how many numbers you want to enter in the list: "))

lst = []
for i in range (1, a+1):
    num = int(input("Enter the Number : "))
    lst.append(num)
print("Original list: ", lst)
lst.sort()
print("Shorted list in ascending order:  ",lst)

