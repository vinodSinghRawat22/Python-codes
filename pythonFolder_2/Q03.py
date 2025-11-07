# 3. Write a program to find the maximum and minimum in a list. 

a = int(input("Enter how many numbers you want to enter in the list: "))

lst = []
for i in range (1, a+1):
    num = int(input("Enter the Number : "))
    lst.append(num)

lst.sort()
print(f"Minimum number in list is : {lst[0]}")
print(f"Maximum number in list is : {lst[a-1]}")