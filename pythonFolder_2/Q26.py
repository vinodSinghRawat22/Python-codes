# 26. Create a function to rotate a list left by k positions. 

def rotate(lst, k):
    
    k = k % len(lst)

    return lst[k:] + lst [:k]

num = int(input("Enter the position to rotate list left : "))
numbers = [ 10, 20, 30, 40, 50]
print("Original list : ", numbers)
print(f"Rotated list left by {num} : {rotate(numbers, num )}")