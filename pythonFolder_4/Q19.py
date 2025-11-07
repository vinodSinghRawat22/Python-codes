# 19. Write a script to clean a text file by removing extra spaces and blank lines. 
try: 
    with open("file19.txt", 'r+') as file: 
        lines = file.readlines()
        cleaned_lines = []
        for line in lines: 
            if line.strip() != "": 
                clean_line = " ".join(line.split())
                cleaned_lines.append(clean_line)



    with open("file19.txt", 'w') as file: 
        for line in cleaned_lines: 
            file.write(line+"\n")
    print("File cleaned successfully")

except Exception as e: 
    print(f"Error occoured as {e}")

