# 
# 1. Create a program that finds the first non-repeating character in a string. 

def character_count(string):
    s = string.lower()
    count = {}
    for ch in s : 
        if ch in count: 
            count[ch] += 1
        else:    
            count[ch] = 1
    for ch in s: 
        if count[ch] == 1:
            print("The first non-repeating character in a string is : ", ch)
            return
    print("No non-repeating character is found")


string1 = input("Enter the string : ").lower()
character_count(string1)


