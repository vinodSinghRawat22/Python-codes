# 07. Write a program to calculate the average word length in a sentence. 

string = input("Enter the string : ")
words = string.split()

length = sum(len(word) for word in words)

avg = length/len(words)
print ("The average word length in a sentence is : ", avg)

