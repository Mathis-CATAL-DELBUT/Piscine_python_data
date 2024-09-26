import sys

try:
    assert len(sys.argv) == 2
except AssertionError:
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
    exit(1)

try:
    arg = int(sys.argv[1])
except ValueError:
    arg = sys.argv[1]

try:
    assert type(arg) is int
except AssertionError:
    print("AssertionError: argument is not an integer")
    exit(1)


if int(sys.argv[1]) % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
