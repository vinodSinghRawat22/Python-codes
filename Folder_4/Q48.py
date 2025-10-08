# 48. Write a Python program to count the frequency of each word in a file. 
import string

with open("file48.txt", "r") as fb: 
    content = fb.read().lower()

words = [word.strip(string.punctuation).lower() for word in content.split()]
freq =  {}
for word in words:
    if word in freq:
        freq[word]+=1 
    else: 
        freq[word] = 1
print("Frequency of each word in file is : ")
for key, value in freq.items():
    print(f"  {key}  :  {value}")