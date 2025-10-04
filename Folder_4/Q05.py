# 05. Write a Python program to find and replace text in a file. 

old_text = input("Enter the old text which you want to replace : ")
new_text = input("Enter the new text: ")

with open("file5.txt", 'r+') as file:
    content = file.read()
    new_content = content.replace(old_text, new_text)
    file.seek(0)
    file.write(new_content)
    file.truncate()
    print("Text replaced successfully.")
    print("The file data after replacement is: ")
    file.seek(0)
    print(file.read())

