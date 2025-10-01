# 4. Create a program that removes duplicates from a list. 

a = int(input("Enter how many numbers you want to enter in the list: "))

lst = []
for i in range (1, a+1):
    num = int(input("Enter the Number : "))
    lst.append(num)

clean_list = list(set(lst))

print(f"Original list :")
print(f"After removing duplicate elements list is: {clean_list}")