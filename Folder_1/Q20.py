# Q20. Create a program to find the second largest number in a list.

lst = [1, 2, 3, 5, 6, 7, 8, 45, 9]
lst = list(set(lst))
lst.sort()

print(f"Second largest number in the list is : {lst[-2]}")


# or.....


largest = lst[0]

for i in range( 1, len(lst)):
    if largest < lst[i] :
        largest = lst[i]

lst.remove(largest)

second_largest = lst[0]

for i in range( 1, len(lst)):
    if second_largest < lst[i] :
        second_largest = lst[i]

print(f"Second largest element in the list is: {second_largest}")


