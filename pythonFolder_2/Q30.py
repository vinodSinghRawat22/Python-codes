# 30. Create a function to find unique elements present in only one of two lists. 


def unique_element(lst1, lst2):
    A = set(lst1)
    B = set(lst2)
    return list(A-B) , list(B-A)



list1 = [1,  2, 3, 4, 5, 1]
list2 = [4, 5, 6,]

unique1 , unique2 = unique_element(list1, list2)

print("Unique element in list 1: ", unique1 )
print("Unique element in list 2 ", unique2)

