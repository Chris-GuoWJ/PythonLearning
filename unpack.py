'''
first, last = input("What's your name? ").split(" ")
print(f"hello, {first}")
'''

'''
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

# *coins1自动解包列表，展开为三个数值"100, 50, 25"
coins1 = [100,50,25]
# **coins2自动解包字典为"galleons = 100, ..."
coins2 = {"galleons": 100, "sickles": 50, "knuts": 25}


print(total(*coins1), "Knuts")
print(total(**coins2), "Knuts")
'''
# 可变参数
def f(*args, **kwargs):
    #print("Positional:", args)
    print("Named:", kwargs)

# f(100, 50, 25)
f(galleons=100)