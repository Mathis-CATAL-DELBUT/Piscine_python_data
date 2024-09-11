import sys
try:
    assert len(sys.argv) == 2
except:
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
    exit(1)
try:
    arg = int(sys.argv[1])
    assert arg == int(sys.argv[1])
except:
    print("AssertionError: argument is not a integer")
    exit(1)

if int(sys.argv[1]) % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")