# 14. Write a function to find common elements in two lists. 

list1 = [1, 3, 5, 7, 9]
list2 = [2, 3, 4, 5, 6]
common = []
for element in list1: 
    if element in list2: 
        common.append(element)
    else: 
        continue 
print(f"Common element in {list1} and {list2} are: ")
for n in common: 
    print( n ,end =' ' )