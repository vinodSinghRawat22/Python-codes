# 28. Write a program to remove all None values from a list. 

my_list = [1, None, 2, None, 3, 4, None, 5]

clean_list = [item for item in my_list if item is not None]

print("Original list : ", my_list)
print("\nCleaned list : ", clean_list)

