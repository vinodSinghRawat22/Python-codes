# 44. Write a Python program to split a sentence into words and reverse each word. 

sentence = input("Enter a sentence: ")

words = sentence.split()
reverse_words = []

for word in words: 
    reverse_words.append(word[::-1])

reverse_words_sentence = " ".join(reverse_words)
print("Sentence after reversing each word is: ",reverse_words_sentence)