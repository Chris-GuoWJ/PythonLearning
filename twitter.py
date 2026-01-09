#re.sub(pattern,repl,string,count=0,flags=0)
import re

url = input("Your URL: ")

username1 = url.removeprefix("https://twitter.com/")
username2 = url.replace("https://twitter.com/","")
print(f"Username1: {username1}")
print(f"Username2: {username2}")

matches = re.search(r"^(?:https?://)?(?:www.)?twitter\.com/(.+)$",url,re.IGNORECASE)
if matches:
    print(f"Username: ",matches.group(1))


username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)
