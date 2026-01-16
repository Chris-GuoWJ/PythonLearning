def main():
    n = int(input("What's n? "))
    for s in sleep(n):
        print(s)

# generator iterator
def sleep(n):
    #只生成一组少量数据，不会一次性生成，不需要等待完全完成
    for i in range(n):
        yield "Sheep" * i

if __name__ == "__main__":
    main()