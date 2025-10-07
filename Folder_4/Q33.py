# 33. Write a function to count how many times a substring appears in a string. 


def count(s, subS):
    s2= s.split()
    count = 0 
    i = 0
    while i<= len(s) - len(subS): 
        if s[i:i+len(subS)] == subS:
            count+=1
            i+= len(subS)
        else: 
            i+=1

    return count 

string = input("Enter a string: ")
subString = input("Enter a sub-string: ")
number = count(string, subString)
print(f"{subString} appers {number} times." )