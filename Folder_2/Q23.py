# 23. Create a nested dictionary to represent students records. 

# operation on pre defined dictonary ::.................

students = {
    "101": {
        "name": "Vinod",
        "age": 19,
        "class":"12th",
        "marks": {"Math": 85, "Python": 90, "Computer": 95}
    },
    "102": {
        "name": "Nandini",
        "age": 18,
        "class":"12th",
        "marks": {"Math": 78, "English": 88, "Computer": 80}
    },
    "103": {
        "name": "Aayush",
        "age": 17,
        "class":"11th",
        "marks": {"Math": 92, "English": 81, "Computer": 89}
    }
}

for i_d, details in students.items():
    print(f"\nRoll No. : {i_d} ")
    for key, value in details.items():
        print(f" {key}: {value}")


# By taking input dictonery from user .........................

students = {}

num = int(input("Number of students : "))

for i in range ( 1, num +1) :
    print(f"Enter the details for students {i} : ")
    roll_no = int(input(" Roll_number : "))
    name = input(" Name :")
    Class = int(input(" Class : "))

    marks = {}
    subject_no = int(input(" Number of subjects : "))
    for i in range (1, subject_no+1) :
        subject_name = input(f"  Subject name {i} : ")
        subject_marks = int(input(f"  Subject marks {i}: "))
        marks[subject_name] = subject_marks

    students[roll_no] = {
        "Name" : name,
        "Class" : Class,
        "Marks" : marks 
    }

for i_d, details in students.items():
    print(f"\nRoll No. : {i_d} ")
    for key, value in details.items():
        print(f" {key}: {value}")
