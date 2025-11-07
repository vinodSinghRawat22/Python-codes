# 21. Create a list comprehension to get squares of all even numbers in a range. 

lower_limit = int(input("Enter lower limit of range : "))
upper_limit = int(input("Enter uppar limit of range : "))

square_of_even = [x**2 for x in range (lower_limit, upper_limit) if x%2==0]
print("list : ", square_of_even)