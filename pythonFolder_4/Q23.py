# 23. Write a script to count the frequency of each character in a string. 

string = input ("Enter the string: ").lower().strip().replace(" ", '')
freq = {}

for ch in string :
    if ch in freq: 
        freq[ch]+=1
    else:
        freq[ch] = 1
print("Frequency of elements in string: ")
for key , value in freq.items():
    print (f"{key} : {value}")

    