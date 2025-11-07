# Q22. Create a program to print all Armstrong numbers between 1 to 1000.

print("Amstrong numbers between 1 to 1000 are")
for num in range( 1, 1000):

    power = len(str(num))

    add = 0
    for i in str(num): 
        add+= int(i)**power

    if int(num) == add: 
        print(num , end= ' ')

