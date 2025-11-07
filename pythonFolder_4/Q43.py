# 43. Create a script that takes a sentence and removes all stop words. 

sentence = input("Enter a sentence: ").lower()

words = sentence.split()
stop_words = ["is", "am", "are", "the", "a", "an", "and", "of", "in", "on", "to", "for", "with", "that", "this", "it", "at", "by", "from"]

filtered_words = [word for word in words if word not in stop_words]
modified_sentence = " ".join(filtered_words)

print(f"Sentence after removing stop words : {modified_sentence}")
