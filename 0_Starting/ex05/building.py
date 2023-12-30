import sys


def get_input():
    """Gets input from the user"""
    string = ''
    try:
        string = input("What is the text to count?\n")
        string += '\n'
    except EOFError:
        pass
    return string


def main():
    """Parses a text and prints the number of each type of character it has"""
    punct = r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    if (len(sys.argv) > 2):
        print("AssertionError: more than one argument is provided")
        exit()
    if (len(sys.argv) == 1 or sys.argv[1] is None):
        string = get_input()
    else:
        string = sys.argv[1]
    print(f"The string contains {len(string)} characters:")
    print(f"{sum(1 for c in string if c.isupper())} upper letters")
    print(f"{sum(1 for c in string if c.islower())} lower letters")
    print(f"{sum(1 for c in string if c in punct)} punctuation marks")
    print(f"{sum(1 for c in string if c.isspace())} spaces")
    print(f"{sum(1 for c in string if c.isdigit())} digits")
    exit()


if __name__ == "__main__":
    main()
