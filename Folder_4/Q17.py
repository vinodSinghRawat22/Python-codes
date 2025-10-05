# 17. Write a script that finds the longest sentence in a paragraph. 

paragraph = input ("Enter paragraph : ")

sentences = paragraph.split('.')

longest_sentence = max(sentences,key=len )

print(f"The longest sentence is : \n  {longest_sentence}")


# without max function:

# length = 0
# longest_sentence = ""

# for sentence in sentences: 
#     if len(sentence) > length: 
#         length = len(sentence)
#         longest_sentence = sentence 
# print("Longest sentence is : ", longest_sentence)
