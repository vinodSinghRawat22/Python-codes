# Q4. Write a program to handle file not found error.
try:
    with open("file4.txt", 'r') as file:
        data = file.read()
    print(data)

except FileNotFoundError:
    print("File not found")

except Exception as e:
    print(f"An error occurred: {e}")    


   