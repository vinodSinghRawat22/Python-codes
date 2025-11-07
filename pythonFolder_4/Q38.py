# 38. Create a program that counts words, characters, and lines in a paragraph. 

paragraph = input("Enter paragraph: ")


words = paragraph.split()
lines = [line for line in paragraph.split(".") if line.strip() != ""]

characters_count = 0 
words_count = len(words) 
lines_count = len(lines)
for ch in paragraph: 
    characters_count+=1

print(f"Number of characters: {characters_count}")
print(f"Number of Words: {words_count}")
print(f"Number of lines: {lines_count}")