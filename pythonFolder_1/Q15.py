# Q15. Create a program to print the Fibonacci series up to N terms.

num = int(input("Enter how many terms you want in fibonacci series: "))

term1 ,term2  = 0 , 1 

if num<=0:
    print("Enter positive number !!")

elif num == 1:
    print("Fibonacci series upto 1 term is:",term1)

elif num == 2:
    print("Fibonacci series upto 2 terms is:", term1 , term2)

else:
    print(f"Fibonacci series upto {num} terms is:", end=' ')

    for i in range (num):
        print(term1 , end= ' ')

        term1, term2 = term2 , term1 + term2