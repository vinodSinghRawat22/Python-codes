# 17. Write a function to count vowels in a string. 

def vowels(s):
    count = 0 
    for ch in s.lower() :
        if ch in 'aeiou': 
            count+=1
    print(f"Number of vowels in str \" {s} \"  : {count}")

string = input("Enter string : ")
vowels(string)