# 16. Write a program that converts a sentence to Pig Latin. 

def pig_latin(w): 
    vowels = 'aeiouAEIOU'
    if w[0] in vowels: 
        return w+ "way"
    else: 
        for i , ch in enumerate(w): 
            if ch in vowels: 
                return w[i:]+w[:i]+'ay'
        return w+'ay'



sentence = input("Enter the sentence:  ")
words = sentence.split()

pig_latin_words = [pig_latin(word) for word in words]

new_sentence = " ".join(pig_latin_words)
print (f"In pig latin the sentence is : {new_sentence}")
