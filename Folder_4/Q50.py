# 50. Write a function to remove punctuation from a string. 

import string

def remove_punctuation(st):
    corrected_string  = ""
    for char in st:
        if char not in string.punctuation:
            corrected_string += char
    return corrected_string


text = input("Enter a string: ")
print("String after removing punctuations : ", remove_punctuation(text))