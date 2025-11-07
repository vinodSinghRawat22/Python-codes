# Q6. Use a list comprehension to filter even numbers from a list.

lst = [1,2,3,4,5,6,7,8,9,10]

evenNumbers = [num for num in lst if num%2 ==0]

print(evenNumbers)