# Q2. Create a file and write your name into it.

with open('file2.txt', 'w') as file:
    data = input ("Enter your name: ")
    file.write(data)
