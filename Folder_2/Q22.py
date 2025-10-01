# 22. Write a function to check if a string is an anagram. 

def check_anagram(s1, s2):

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if sorted(s1) == sorted(s2):
        print("Strings are anagram.")
    else:
        print("Strings are not anagram.")

str1 = input("Enter first word : ")
str2 = input("Enter second word : ")

check_anagram( str1, str2 )