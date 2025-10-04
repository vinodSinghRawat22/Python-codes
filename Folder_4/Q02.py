# 
# 2. Write a script that converts camelCase to snake_case. 

def camel_to_snake(text):
    result = ""
    for i, ch in enumerate(text):
        if ch.isupper():
            if i!=0:
                result+= "_"
            result+= ch.lower()
        else:
            result += ch

    return result



camel_case = input("Enter in camel case : ")

print("Camel case : ", camel_case)
print("Snake case : ", camel_to_snake(camel_case))
