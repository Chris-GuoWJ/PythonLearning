'''
email = input("Email: ").strip()

username, domain = email.split("@")

if username and domain.endswith(""):
    print("Valid")
else:
    print("Invalid")
'''

#re.search(pattern,string,flags=0)

import re

email = input("Email: ").strip()

#if re.search(r"^.+@.+\.edu$",email):
#if re.search(r"^[^@]+@[^@]+\.edu$",email):
#if re.search(r"^[a-zA-Z0-9_]+@[^@]+\.edu",email):
if re.search(r"^(\w|\s)+@(\w+\.)?\w+\.(com|cn|edu|org)$",email,re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")