# 1. Write a function to check if a number is even. 

def check_even(a) :
    if a%2 ==0 : 
        print(f"{a} is Even.")
    else:
        print(f"{a} is odd.")

num = int(input("Enter the number: "))
check_even(num)