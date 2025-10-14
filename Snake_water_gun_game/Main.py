# Snake Water Gun
'''

 Snake (s) = 0
 Water (w) =1
 Gun (g)   = 2
 
'''
import random

computer = random.choice([0 ,1, 2])

My_dict = { "s" : 0 , "w" : 1 , "g" : 2}

reverse_dict = {0:"Snake", 1:"Water", 2 : "Gun"}

print()
print("Rules:")
print()
print ("--Type s for Snake ")
print ("--Type w for Water ")
print ("--Type g for Gun ")
print()
you_choice =input("Enter your choice :")
print("__________________________________________")
print()

if (you_choice =="s" or you_choice =="w" or you_choice == "g"):
    you = My_dict[you_choice]
    print(f"You choose --[{reverse_dict[you]}] \nComputer choose --[{reverse_dict[computer]}]")
    print()

    if (you==computer):
        print("Game Draw......!!")
    else :
        if (you == 0 and computer ==1):
            print("You Wom...!!")
        elif (you == 0 and computer ==2):
            print("You Lose...!!")
        elif (you == 1 and computer ==0):
            print("You Lose...!!")
        elif (you == 1 and computer ==2):
            print("You Won...!!")
        elif (you == 2 and computer ==0):
            print("You Won...!!")
        elif (you == 2 and computer ==1):
            print("You Lose...!!")
        else :
            print("Incorrect option ... replay....!!!!!")

    print("_____________________________________________________")
    print()
else:
    print("Incorrect option ... replay....!!!!!")
    print()



    