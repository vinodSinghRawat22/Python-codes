# 26. Write a program that takes a string and returns the string in reverse order without using [::-1]. 

string = input("Enter a string: ")

reverse_string =""
for i in range (len(string)-1,-1, -1):
    reverse_string+=string[i]

# # or
# reverse_string = "".join(reversed(string))

print(f"Original string: {string}")
print(f"Reverse string: {reverse_string}")



