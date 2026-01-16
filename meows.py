import sys

def meow(n: int) -> str:
    '''
    meow 的 Docstring
    
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    '''
    return "meow\n" * n

if len(sys.argv) == 1:
    print(meow(1))
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    print(meow(n), end = "")
else:
    print("You can send 'py meows.py' or append '-n (int)'")



'''
number: int = int(input("Number: "))
print(meow(number), end="")
'''
