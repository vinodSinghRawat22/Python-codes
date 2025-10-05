# 12. Create a function that validates an email address format. 

import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

email_address = input("Enter an email address: ")
if validate_email(email_address):
    print("Valid email address")
else:
    print("Invalid email address")