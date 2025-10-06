# 30. Write a Python program to capitalize the first letter of each word in a sentence. 

sentence = input("Enter a sentence: ")

print("New sentence : ",sentence.title())

# or

words = sentence.split()
capitalized_words = [word.capitalize() for word in words]
capitalized_sentence = " ".join(capitalized_words)
print("New sentence : ",capitalized_sentence)