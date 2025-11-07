# Q18. Check whether a ch is a vowel or consonant.


char = input ("Enter a letter: ")
ch = char.lower()

if ch in 'aeiou' :
     print(f"{char} is vovel")

elif ch in 'bcdfghjklmnpqrstvwxyz':
    print(f"{char} is consonant ")

else:
    print( "Enter a valid letter")

