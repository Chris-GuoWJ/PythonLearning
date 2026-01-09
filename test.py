from practice import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3")

if __name__ == "__main__":
    main()

#CS50P单元测试集20min处开始讲PyTest