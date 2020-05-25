import sys

if (len(sys.argv) == 2):
    try:
        n = int(sys.argv[1])
        if n % 2 and n != 0:
            print("I'm Odd.")
        elif n == 0:
            print("I'm Zero.")
        else:
            print("I'm Even.")
    except ValueError:
        print("ERROR")
else:
    print("ERROR")
