# 29. Write a function to merge two dictionaries and handle key collisions by summing values. 

def merge(d1, d2):
    merged_dict = d1.copy()
    for key, value in d2.items(): 
        if key in merged_dict: 
            merged_dict[key]+= value
        else: 
            merged_dict[key] = value
    return merged_dict
    




dict1 = {'a': 10, 'b': 5, 'c': 7}
dict2 = {'b': 3, 'c': 2, 'd': 8}
print("\nDictonery 1 : ", dict1)
print("\nDictonery 2 : ", dict2)
print("\nMerged dictonery : ", merge(dict1, dict2))