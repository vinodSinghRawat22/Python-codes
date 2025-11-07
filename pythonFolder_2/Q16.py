# 16. Create a function that checks whether a string is a palindrome. 

def palindrome(s): 
    if s.lower().strip() == s[::-1].lower().strip(): 
        print(f"{s} is palindrome")
    else:
        print(f"{s} is not palindrome")

string = input( "Enter the string : ")
palindrome(string)