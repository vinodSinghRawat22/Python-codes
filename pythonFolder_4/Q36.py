# 036. Create a program to filter out all non-alphabetic characters from a string. 

string = input("Enter a string: ")
clean_string = ""

for ch in string: 
    if ch.isalpha():
        clean_string+= ch

print(f"String after filtering out non-alphabetic characters is: {clean_string}")