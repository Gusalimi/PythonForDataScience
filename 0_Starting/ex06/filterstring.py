import sys


def main():
    """output a list of words from argv[1] that have a\
 length greater than argv[2]"""
    try:
        if (len(sys.argv) != 3 or not sys.argv[2].isdigit()):
            raise AssertionError("the arguments are bad")
        lst = sys.argv[1].split()
        new_lst = [w for w in lst if (lambda x: len(x) > int(sys.argv[2]))(w)]
        print(new_lst)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit()


if __name__ == "__main__":
    main()
