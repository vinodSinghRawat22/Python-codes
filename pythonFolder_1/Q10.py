# Q10. Check if a number is a palindrome. 

num = input("Enter Number: ")

reversed_num = num[::-1]

# other method

'''reversed_num = 0
temp = num

while temp > 0:
    digit = temp % 10       
    reversed_num = reversed_num * 10 + digit  
    temp = temp // 10       '''

if num == reversed_num: 
    print("Number is palindrome")
else:
    print("Number is not palindrome")
