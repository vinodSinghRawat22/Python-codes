# Q24. Create a calculator app using if-else.

operation = input("Enter operation symbol (+ | - | * | / ) : ")

numbers = int(input("Enter how many numbers you want to enter: "))   
lst = []
for i in range (1 , numbers+1):
    num = float(input(f"Enter number {i} :")) 
    lst.append(num)
print (lst)
if operation == '+':
    total = 0 
    for i in lst:
        total+=i
    print("Sum of the number is: ", total)

elif operation == '-':
    
    difference = lst[0]
    for i in lst[1:] :
        difference -= i  
    print("Difference of the number is: ", difference)
    
elif operation == '*':
    multiplication = 1
    for i in lst:
        multiplication *= i 
    print("Multiplication of numbers is : ", multiplication)

elif operation =='/' :
    result = lst[0]
    for i in lst[1:]: 
        if i != 0: 
            result /= i

        if i == 0 :
            print("Error: division by zero is not possible")
            break 
    print("Division of numbers is : ", result)
else:
    print("Error: Enter valid operation from (+ | - | * | / ) : ")
    