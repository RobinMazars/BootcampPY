import random
# random.seed(1234)
OK = '\033[94m'
FAIL = '\033[91m'
ENDC = '\033[0m'

r = random.randint(1, 99)
# r = 42
# print(r)
print("This is an interactive guessing game!")
print("You have to enter a number between", end="")
print(" 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
count = 0
while True:
    guest = input("What's your guess between 1 and 99?\n")
    if "exit" == guest:
        print("Goodbye!")
        exit()
    count += 1
    try:
        n = int(guest)
        if n < r:
            print("Too low!")
        elif n > r:
            print("Too high!")
        elif n == r:
            if count == 1:
                if r == 42:
                    print(
                        OK + "The answer to the ultimate question of life,"
                        "the universe and everything is 42." + ENDC)
                print(OK + "Congratulations! You got it"
                      " on your first try!" + ENDC)

            else:
                print(OK + "Congratulations, you've got it !" + ENDC)
                print(f"You won in {count} attempts!")
            break
    except ValueError:
        print(FAIL + "That's not a number" + ENDC)
