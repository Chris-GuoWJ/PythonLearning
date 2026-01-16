def main():
    yell("This", "is", "CS50")

def yell(*words):
    '''
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)
    '''

    '''
    uppercased = [word.upper() for word in words]
    print(*uppercased)
    '''
    
    # map传入函数，对每一个单词进行函数操作，返回一个全新列表
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()