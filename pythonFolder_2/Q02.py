# 2. Create a list and find the sum of all its elements. 

a = int(input("Enter how many numbers you want to enter in the list: "))

lst = []
for i in range (1, a+1):
    num = int(input("Enter the Number : "))
    lst.append(num)

Sum = 0
for i in lst:
    Sum+=i
print(f"Sum of all elements of list is : {Sum}")