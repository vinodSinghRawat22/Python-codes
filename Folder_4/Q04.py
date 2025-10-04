# 04. Write a script to check if a file contains a specific word. 

word = input("Enter the word : ").lower()


try:
    with open("file4.txt", 'r') as file: 
        content = file.read().lower()
        if word in content:
            print("Yes! word is present in the file. ")
        else: 
            print("No! word is not present in the file.")
except Exception as e:
    print(f"An error occured as : {e}")

