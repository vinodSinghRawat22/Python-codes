# 37. Write a function that returns True if a string ends with a given suffix. 

def ends_With(st, suff): 
    s = st.lower().strip()
    sf = suff.lower().strip()

    return s[-len(sf):] == sf if len(suff) <= len(s) else FALSE

string = "Hello world"

suffix = "world"

print(f"String ends with given suffix: ", ends_With(string, suffix))