# 5. Write a function to reverse a list. 

a = int(input("Enter how many numbers you want to enter in the list: "))

lst = []
for i in range (1, a+1):
    num = int(input("Enter the Number : "))
    lst.append(num)
print("\nOriginal list: ", lst)
lst.reverse()
print("\nReversed list: ", lst)


# or..........................

n = len(lst)
for i in range (n//2):
    lst[i], lst[n-i-1] = lst[n-i-1] , lst[i]
print(f"\n Again Revrsed list : {lst} \n ")