# Q9. Write a Python script to reverse a given string.

str = input("Enter String: ")

length = len(str)

for ch in range(length, 0, -1):
    print(str[ch-1], end="")