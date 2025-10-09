from pathlib import Path 


def read_file_and_folder():
    path = Path("")
    items =  list(path.rglob('*'))
    print("These files already exists in this directory : ")
    for i, item in enumerate(items):
        print(f"    {i+1}  :  {item}")

def create_file():
    try:
        read_file_and_folder()
        name = input("Enter the file name to create : ") 
        p = Path(name)
        if not p.exists():
            with open (p , 'w') as fs:
                data = input("Enter what you want to write in file: ")
                fs.write(data)
            print(f"File {name} created successfully")
        else:
            print(f"File {name} already exists")    

    except Exception as e:
        print(f" An error occured as {e}" )

def readFile():
    try:
        read_file_and_folder()
        name = input("Enter the file name which you want to read : ")  
        p = Path(name)
        if  p.exists():
            with open (p , 'r') as fs:
                data = fs.read()
                print(f"\nFile Data is this : ")
                print(f"   {data}")
        else:
           print("\nFile not found")
                
    except Exception as e:
        print(f" An error occured as {e}")
    

def updateFile():
    try:
        read_file_and_folder()
        name = input("Enter the file name which you want to update : ")  
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing file name : ")
            print("Press 2 for overwriting file data : ")
            print("Press 3 for appending data in file : ")
            res = int(input("Enter your choice : "))

            if res == 1:
                new_name = input("Enter new file name : ")
                p2 = Path(new_name)
                if not p2.exists():
                    p.rename(p2)
                    print(f"File name changed from {name} to {new_name}")
                else:
                    print(f"File {new_name} already exists")
            elif res == 2:
                with open (p , 'w') as fs:
                    data = input("Enter what you want to write in file: ")
                    fs.write(data)
                    print("Overwrited successfully")
                print(f"File {name} updated successfully")
            elif res == 3:
                with open (p , 'a') as fs:
                    data = input("Enter what you want to append in file: ")
                    fs.write(data)
                    print("Appended successfully")
                print(f"File {name} updated successfully")
            else:
                print("Invalid choice")
        else:
            print("File not found")
    except Exception as e:
        print(f" An error occured as {e}")


def deleteFile():
    try:
        read_file_and_folder()
        name = input("Enter the file name which you want to delete : ")  
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print(f"File {name} deleted successfully")
        else:
            print("File not found")
    except Exception as e:
        print(f" An error occured as {e}")


print("File handling : ")
print("Press 1 for creating file : ")
print("Press 2 for reading file : ")
print("Press 3 for updating file : ")
print("Press 4 for deleting file : ")

choice = int(input("Enter your choice : "))

if choice == 1:
    create_file()

elif choice == 2 :
    readFile()

elif choice == 3:
    updateFile()

elif choice == 4:
    deleteFile()

else:
    print("Invalid choice")
