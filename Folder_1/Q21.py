# Q21. Write a program to count the number of digits in an integer. 

num = input("Enter the integer: ") 

count = 0 
 
for n in num : 
    if n == '-' :
        continue
    count+=1

print(f"Number of digits in the integer {num} is: {count}")
    
# or...............

count = len(str(abs(int(num))))
print(f"Number of digits in the integer {num} is: {count}")