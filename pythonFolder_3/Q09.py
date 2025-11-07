# Q9. Write a program to read a CSV file and print its contents. 

import csv
try:
    with open('file9.csv', 'r') as file :
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error occurred: {e}")