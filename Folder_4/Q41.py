# 41. Create a script to convert binary string to decimal. 

binary_string = input("Enter binary string: ")

decimal_string = str(int(binary_string,2))

# or

decimal_num = 0 
for num in binary_string:
    decimal_num = decimal_num*2 + int(num)

print(f"After conversion of binary string into decimal is: {decimal_num}")

print(f"After conversion of binary string into decimal is: {decimal_string}")