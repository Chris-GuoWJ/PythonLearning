import re

name = input("Name: ").strip()
print(f"hello, {name}")

if matches := re.search(r"^(.+), *(.+)$",name):
    last, first = matches.groups()
    name = matches.group(2) + " " + matches.group(1)

#if "," in name:
#    last,first = name.split(",")
#    name = f"{first} {last}"
print(f"hello, {name}")