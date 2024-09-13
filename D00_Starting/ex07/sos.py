import sys

NESTED_MORSE = {
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    " ": "/ ",
}


def main():
    try:
        assert len(sys.argv) == 2
        assert all(letter.isalnum() or letter == " " for letter in sys.argv[1])
    except AssertionError:
        print("AssertionError: the arguments are bad")
        exit(1)
    result = ""
    string = sys.argv[1].upper()
    for letter in string:
        result += NESTED_MORSE[letter]
    result = result[:-1]
    print(result)


if __name__ == "__main__":
    main()
