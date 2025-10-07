# 35. Write a Python program to merge two dictionaries into one. 

# Another example of simple dictionaries
dict1 = {
    "name": "Alice",
    "age": 20
}

dict2 = {
    "city": "New York",
    "country": "USA"
}


merged_dict = dict1.copy()
merged_dict.update(dict2)

print(f"Merged dictonery is: {merged_dict}")