# Q7. Write a generator that yields even numbers up to N.

number= int  (input("Enter a number upto which you want to print even numbers: " ))

for num in range (0, number+1):
    if num % 2 == 0:
        print(num)
    else:
        continue