import sys


def main():
    """
    Main function of the program
    """

    if len(sys.argv) != 2:
        print("the program takes 1 argument as parameter")
        exit(1)
    string = sys.argv[1]
    lenght = len(string)
    lowers, uppers, ponctuations, spaces, digits = count(string, 0, 0, 0, 0, 0)

    print(f"The text contains {lenght} characters:")
    print(f"{uppers} upper letters")
    print(f"{lowers} lower letters")
    print(f"{ponctuations} ponctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def count(string, lowers, uppers, ponctuations, spaces, digits):
    """
    Count the number of lower letters, upper letters, ponctuation marks,
    spaces and digits in a string
    """
    for letter in string:
        if letter.islower():
            lowers += 1
        elif letter.isupper():
            uppers += 1
        elif letter.isdigit():
            digits += 1
        elif letter.isspace():
            spaces += 1
        else:
            ponctuations += 1
    return lowers, uppers, ponctuations, spaces, digits


if __name__ == "__main__":
    main()
