# 24. Write a function to flatten a nested list. 


def flatten_nested_list(n_list):
    
    flat_lst = [item for sublist in n_list for item in sublist]
    
    return flat_lst


nested_list = [ [1, 2, 3], [4, 5], [6, 7, 8, 9] ]
print("Original list : ", nested_list)
print("Flatten nested list :  ",flatten_nested_list(nested_list))
