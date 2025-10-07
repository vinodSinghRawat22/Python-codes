# 39. Write a script to encode a string using Caesar cipher (shift = 3). 
def caesar_cipher(text, shift=3):
    
    result = ""
    
    for char in text:
        if char.isalpha(): 
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


text = input("Enter text: ")
encoded_text = caesar_cipher(text)
print(f"Original: {text}")
print(f"Encoded: {encoded_text}")
