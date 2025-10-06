# 25. Create a program to find the longest word in a sentence. 

sentence =  input ("Enter a sentence: ")
lst = sentence.split()
largest = lst[0]
for word in lst: 
    if len(word)> len(largest):
        largest = word 


print(f"Longest word in string is : {largest}")