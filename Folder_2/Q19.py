# 19. Write a function to remove all punctuation from a string. 

def remove_punctuations(s):
    punctuation = ['.', ',', '?', '!', ':', ';', "'", '"', '-', '(', ')', '…', '/']
    for p in punctuation: 
        s = s.replace( p , '')

    print(f"After removal : {s}")

string = input("Enter string : ")
print(f"Original string : {string}")
remove_punctuations(string)