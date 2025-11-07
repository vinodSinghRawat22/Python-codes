# 15. Create a script to find duplicate words in a paragraph. 

text = input("Enter text: ")

words = text.split()
duplicates = []
unique = []

for word in words:
    if word in unique:
        duplicates.append(word)    
    else:
        unique.append(word)

print("Duplicate words:", duplicates)


