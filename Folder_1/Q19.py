# Q19. Write a program to calculate the sum of digits of a number.

num = input("Enter a number: ")

sum = 0
for n in num :
    sum += int(n)

print(f"Sun of the digits of number {num} is: {sum}")