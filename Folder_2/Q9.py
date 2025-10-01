# 9. Write a function to count the frequency of elements in a list. 

a = int(input("Enter how many numbers you want to enter in the list: "))

lst = []
for i in range (1, a+1):
    num = int(input("Enter the Number : "))
    lst.append(num)


feq_dict = {}

for item in lst: 
    if item in feq_dict: 
        feq_dict[item]+= 1
    else: 
        feq_dict[item] = 1

print(f"Frequency of elements in list {lst} : ")
for key, value in feq_dict.items():
    print(f"{key} occurs {value} time.")
