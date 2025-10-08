# 46. Write a program to find all palindromic substrings in a string. 

def palindromic_substrings(s):
    palindrom = set()
    n = len(s)

    for start in range(n):
        for end in range(start+1, n+1):
            substring = s[start:end]
            if substring == substring[::-1]: 
                palindrom.add(substring)
    return palindrom

text = input("Enter a string: ")
result = palindromic_substrings(text)

if result: 
    print("Palindromic substrings found:")
    for p in sorted(result):
        print(p)
else: 
    print("No palindromic substrings found.")