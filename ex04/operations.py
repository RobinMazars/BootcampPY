import sys


def displayUsage():
    print("Usage: python operations.py <number1> <number2>")
    print("Example:\n\tpython operations.py 10 3")


if (len(sys.argv) == 3):
    try:
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[2])
        print(f"Sum:\t\t{n1+n2}")
        print(f"Difference:\t{n1-n2}")
        print(f"Product:\t{n1*n2}")
        if n2 != 0:
            print(f"Quotient::\t{n1/n2}")
            print(f"Remainder:\t{n1%n2}")
        else:
            print("Quotient::\tERROR (div by zero)")
            print("Remainder:\tERROR (modulo by zero)")
    except ValueError:
        print("InputError: only numbers\n")
        displayUsage()
elif (len(sys.argv) == 1):
    displayUsage()
elif (len(sys.argv) == 2):
    print("InputError: not enough arguments\n")
    displayUsage()
elif (len(sys.argv) > 3):
    print("InputError: too many arguments\n")
    displayUsage()
