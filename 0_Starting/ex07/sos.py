import sys


def main():
    """Converts argv[1] to morse code"""
    try:
        if (len(sys.argv) != 2 or not ''.join(sys.argv[1].split()).isalnum()):
            raise AssertionError("the arguments are bad")
        morse = {
            ' ': '/', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
            'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
            'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
            '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.'
        }
        string = sys.argv[1].upper()
        for (c) in string:
            if (c not in morse):
                raise AssertionError("the arguments are bad")
            print(morse[c], end=(' ' if c != string[len(string) - 1] else ''))
        print()
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
