# 11. Write a program that counts the occurrence of each vowel in a paragraph. 

text = input("Enter the paragraph: ").upper()

vowels = "AEIOU"
vowel_count = {}

for vowel in vowels:
    count = text.count(vowel)
    vowel_count[vowel] = count

print("Occurrence of each vowel:")
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")