# Q26. Convert a decimal number to binary using loops. 

num = int(input("Enter a decimal number: "))

binary = ""

if num == 0:
    binary = "0"
else:
    while num > 0 :
        reminder = num % 2
        binary = str(reminder) + binary
        num = num // 2

print(F"{num} in binary is : {binary}")