# Q13. Write a program to print all prime numbers between 1 and 100.

for num in range (2, 100):
    for i in range(2,num+1):
        if num % i == 0 :
            if num == i:
                print (num)
            break 
