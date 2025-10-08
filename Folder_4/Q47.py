# 47. Write a function that compresses a string using run-length encoding. 

def length_encode(s):
    
    encoded = ""
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count+=1
        else:
            encoded += f"{current_char}{count}"
            current_char = char
            count = 1
    encoded += f"{current_char}{count}"
    return encoded


string = input("Enter a string: ")
result = length_encode(string)
print(f"String after encoding : {result}")
