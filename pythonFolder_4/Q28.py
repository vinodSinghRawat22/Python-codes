# 28. Write a Python script to sort words in a sentence alphabetically. 

sentence = input("Enter a sentence: ")

words = sentence.split()
sorted_words = sorted(words, key= str.lower)
sorted_sentence = " ".join(sorted_words) 

print(f"Sorted sentence: {sorted_sentence}") 
