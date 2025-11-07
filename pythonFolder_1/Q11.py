# Q11. Write a program to find the sum of first N natural numbers. 

num = int(input("Enter how many natural numbers sum you want: "))

sum = 0;
for i in range (1, num+1 ):
    sum+=i
print(f"Sum of first {num} natural numbers is : {sum}")