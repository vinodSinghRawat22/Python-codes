# Q12. Create a number guessing game. 

import random

choice = 1

while choice == 1:

    num = int(input("\nGuess the number betwee [1 to 10] : "))

    guess_num = random.randint(1, 10)

    if num == guess_num :
        print(f"\nCorrect Guess ..... No is {num}")

    else:
        print(f"\nWrong guess.... Correct number is {guess_num}  and your guess is {num}")

    choice = int(input("\nTo continue enter 1 otherwise 0 :"))