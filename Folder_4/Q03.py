# 3. Write a function to generate acronyms from a sentence.

def acronyms_generator(line):
    words = line.split()
    acronyms = ""
    skip_words = ["and", "the", "of", "in", "on", "at", "to", "for", "with"]
    for i in words: 
        if i.lower() not in skip_words: 
            acronyms += i[0].upper()
    return acronyms


sentence = input("Enter the sentence : ")
print(f"The acronyms from sentence [{sentence}] is : ", acronyms_generator(sentence))
