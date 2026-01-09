#在terminal里可以用tab一键补全

#programme1
'''
name = input("Enter: ")
name1 = name.strip().title()
#去除前后空格并让每个单词变为标题模式也就是首字母大写

name2 = name.capitalize()
first,last = name.split()
print(name,name1,name2,sep = " and ",end = " ")
print(first, last)
print(f"Name: {name1}")
'''

#programme2
'''
x = int(input("x = "))
y = int(input("y = "))
#input 输入的是文本而不是数字
z = x + y
a = 0.456
b = round(0.6)
#round(number[,ndigits])，四舍六入五在个位为偶数时不入
print(z,a,b)
print(f"{a:.2f}")
c = 1000
print(f"{c:,}")
#千位符
'''

#Programme3
'''
def main():
    name = input("Name:").strip().title()
    hello(name)
    hello()

def hello(to="everyone"):
    print("hello!",to)

main()
'''

#Programme4
'''
x = int(input("x = "))
y = int(input("y = "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x equals to y")
'''

#Programme5
'''
def main():
    x = int(input("x = "))
    if isEven(x):
        print("Even")
    else:
        print("odd")

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()
'''

#Programme6
'''
def is_even(n):
    return True if n % 2 == 0 else False
def is_even2(n):
    return n % 2 == 0
'''

#Programme7
'''
name = input("Name: ").strip().title()

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Not Founded")
'''

#Programme8
'''
for _ in range(3):
    print("OK")
#打印3次OK，用_更加pythonic，表示一个无需在意命名的工具值

print("OK\n"*3,end = "")
'''

#Programme9
'''
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("number = "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")
    
main()
'''

#Programme10
'''
students1 = {
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin",
}

for student1 in students1:
    print(student1,students1[student1],sep = ", ")
#字典进阶用法
students2 = [
    {"name":"Hermione","house":"Gryffindor","patronus":"Otter"},
    {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
]

for student2 in students2:
    print(student2["name"],student2["house"],sep = ", ")
'''

#Programme11
#防御性编程
'''
try:
    x = int(input("What's x: "))
except ValueError:
    print("x should be an integer")
else:
    print(f"x is {x}")
'''

#Programme12
#循环提示
'''
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x: "))
        except ValueError:
            print("x should be an integer")

main()
'''

#Programme13
'''
while True:
    try:
        x = int(input("What's x: "))
        break
    except ValueError:
        pass
print(f"x is {x}")
'''

#Programme14
'''
def main():
    x = get_int("What's x: ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x should be an integer")

main()
'''


#Programme15
'''
import random
for _ in range(5):
    coin = random.choice(["heads","tails"])
    print(coin)

    number = random.randint(1,10)
    print(number)
'''

#Programme16
'''
from random import choice
for _ in range(5):
    coin = choice(["0","1"])
    print(coin)
'''


#Programme17
'''
import random

cards = ["j", "q", "k"]
#随机打乱列表
random.shuffle(cards)
for card in cards:
    print(card)
'''

#Programme18
'''
import statistics

print(statistics.mean([100,90]))
'''


#Programme19
'''
import sys
#在命令行用命令运行时在后面加名字
#如：python xxx.py Chris
if len(sys.argv) > 2:
#提前退出
    sys.exit("Too many arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few arguments")

print("hello, my name is",sys.argv[1].strip().title())
'''


#Programme20
'''
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
#slice切片的应用
for arg in sys.argv[1:]:
    print("hello, I'm",arg)
'''


#Programme21
#需预先下载requests包，json为系统自带
'''
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term="+sys.argv[1])

o = response.json()
print(json.dumps(response.json(), indent=2))

for result in o["results"]:
    print(result["trackName"])
'''
#CS50P 函数库集中1h10min开始，详细内容


#Programme22
'''
def main():
    x = int(input("x = "))
    print("x squared is",square(x))

def square(n):
    return n+n

print(__name__)

#此处详见浏览器Python收藏夹相关介绍
if __name__ == "__main__":
    main()
'''

#Programme23
'''
names = []

for _ in range(3):
    name = input("Name:")
    #append函数，在列表末尾添加元素
    names.append(name)

for name in sorted(names):
    print(f"Hello, {name}")
'''


#Programme24
'''
name = input("Name:")
#每次使用w写入模式会重新创建文件，类似初始化!!
# file = open("name.txt","w")
#append
file = open("name.txt","a")
file.write(f"{name}\n")
file.close()
'''

#Programme25
'''
name = input("Name:")

with open("name.txt","a") as file:
    file.write(name)
#退出with自动关闭file
'''

#Programme25
#sorted(iterable,/,*,key=None, reverse=False)
'''
with open("name.txt","r") as file:
    for line in sorted(file):
        print("hello",line.rstrip())
'''


#Programme26
'''
infos =[]
for _ in range(3):
    info = input("name&age&sex:")
    infos.append(info)

with open("infos.csv","w") as file:
    for info in sorted(infos):
        file.write(f"{info}\n")
'''


#Programme27
'''
infos = []
with open("infos.csv") as file:
    for line in file:
        #row = line.rstrip().split(",")
        #print(f"{row[0]},{row[1]},{row[2]}")
        name,age,sex = line.rstrip().split(",")
        info = {}
        info["name"] = name
        info["age"] = age
        info["sex"] = sex
        infos.append(info)

def get_age(info):
    return info["age"]
#key传入函数（以下两种方式均可，第一种更好，lambda是固定名字，意思是匿名函数）
#for student in sorted(students, key=lambda student: student["name"]):
for info in sorted(infos,key=get_age):
    print(f"{info['name']}, {info['age']}, {info['sex']}")
'''

#Programme28
'''
import csv

infos = []

with open("infos.csv") as file:
    reader = csv.reader(file)
    for name,age,sex in reader:
        infos.append({"name":name,"age":age,"sex":sex})

for _ in sorted(infos,key=lambda info:info["age"]):
    print(f"{_["name"]},{_["age"]},{_["sex"]}")
'''
#文件I/O集1h10min左右DictReader

#Programme29
'''
import csv

infos = []

with open("infos.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        infos.append(row)

for info in sorted(infos, key=lambda info:info["age"]):
    print(f"{info['name']},{info['age']},{info['sex']}")
'''


#Programme30
'''
import csv

name = input("name:")
age = input("age:")
sex = input("sex:")

#with open("infos.csv","a") as file:
#    writer = csv.writer(file)
#    writer.writerow([name,age,sex])

with open("infos.csv","a") as file:
    writer = csv.DictWriter(file,fieldnames=["name","age","sex"])
    writer.writerow({"name":name,"sex":sex,"age":age})
'''

#Programme31
#gif generator
'''
import sys
#需要pillow库
from PIL import Image

images = []

for arg in sys.argv[1:]:
    #从命令行接受多个地址
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif",save_all=True,append_images=[images[1]],duration = 200,loop=0
)
'''


