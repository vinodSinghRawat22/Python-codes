# Q28. Write a program to find the sum of all even numbers in a list. 

lst = []
num = int(input("Enter the no. of digits you want to enter in list: "))

for i in range(1,num+1):
    number = int(input(f"Enter the number {i}: "))
    lst.append(number)

total = 0 
for i in lst:
    if i % 2 == 0: 
        total+= i
print(f"Sum of even number in list is: {total}")