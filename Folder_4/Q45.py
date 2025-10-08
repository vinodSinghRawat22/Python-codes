# 45. Write a function that returns a new string made of every third character of the original string. 

def string_modify(st):
    new_str = ""
    for i in  range (0,len(st),3):
        new_str+= st[i]
    return new_str
    #or
    #return st[::3]

string = input("Enter a string: ")
print("String after modification: ", string_modify(string))

