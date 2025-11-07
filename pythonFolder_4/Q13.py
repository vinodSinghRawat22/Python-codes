# 13. Write a script to check if a string is a valid URL. 

import re

def url_validator(u):
    pattern = r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/\S*)?$'
    if re.match(pattern , u): 
        print("Valid URL")
    else: 
        print("Invalid URL")


url = input("Enter URL: ")
url_validator(url)

# Example URLs to test:
# Valid: https://www.example.com, http://example.com, www.example.com/path
# Invalid: https://example, http://.com, www.example, example.com/