import sys


def filterstring(string, i):
    """
    Filter the words of a string that have a length greater than i
    """
    tab = []
    words = string.split()
    for word in words:
        if len(word) > i:
            tab.append(word)
    return tab


def main():
    """
    Main function of the program
    """

    try:
        first = sys.argv[1]
        second = int(sys.argv[2])
    except ValueError:
        first = -1
        second = None

    try:
        assert len(sys.argv) == 3
        assert type(first) is str
        assert type(second) is int
    except AssertionError:
        print("AssertionError: the arguments are bad")
        exit(1)
    print(filterstring(sys.argv[1], int(sys.argv[2])))


if __name__ == "__main__":
    main()
