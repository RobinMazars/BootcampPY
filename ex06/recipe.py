from pprint import pprint

OK = '\033[94m'
FAIL = '\033[91m'
ENDC = '\033[0m'


def display_quest():
    print(OK + "Please select an option by typing the corresponding number")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit" + ENDC)


def display_recipe(rec):
    print(f"Recipe for {rec}:", sep="")
    print(f"Ingredients list: {cookbook[rec]['ingredients']}")
    print(f"To be eaten for {cookbook[rec]['meal']}.", sep="")
    print(f"Takes {cookbook[rec]['prep_time']} minutes of cooking.")


def cookbook_add(name, ing, meal, time):

    recip = {"ingredients": list_ingr,
             "meal": meal, "prep_time": time
             }
    cookbook.update({name: recip})


def cookbook_del(rec):
    cookbook.pop(rec)


def display_cookbook():
    for x in cookbook:
        display_recipe(x)
        print()


sandwich = {"ingredients": ["ham", "bread", "cheese", "tomatoes"],
            "meal": "lunch",
            "prep_time": 10
            }
cake = {"ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
        }
salad = {"ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
         "meal": "lunch",
         "prep_time": 15
         }
cookbook = {}
cookbook.update({'sandwich': sandwich})
cookbook.update({'cake': cake})
cookbook.update({'salad': salad})
pprint(cookbook)
print(cookbook)

display_quest()
while 1:
    choice = input()
    if choice == "1":
        name = input("Please enter the recipe's name to add:\n")
        count = 0
        list_ingr = []
        while 1:
            print("Please enter the ingredients's ", end="")
            print(f"name n°{count} :(type exit for finish)")
            ing = input()
            if ing == "exit":
                break
            else:
                count += 1
                list_ingr.append(ing)
        meal = input("Please enter type of meal:\n")
        time = input("Please enter preparation time in minutes:\n")
        cookbook_add(name, list_ingr, meal, time)
        print()
        display_recipe(name)
        print()
        display_quest()
    elif choice == "2":
        rec = input("Please enter the recipe's name to delete:\n")
        if rec in cookbook:
            cookbook_del(rec)
        else:
            print(FAIL + f"Recipe : {rec} not found.\n" + ENDC)
        display_quest()
    elif choice == "3":
        rec = input("Please enter the recipe's name to get its details:\n")
        if rec in cookbook:
            display_recipe(rec)
        else:
            print(FAIL + f"Recipe : {rec} not found.\n" + ENDC)
        display_quest()
    elif choice == "4":
        display_cookbook()
        display_quest()
    elif choice == "5":
        print("Cookbook closed.")
        break
    else:
        print("This option does not exist, ", end="")
        print("please type the corresponding number.")
        print("To exit, enter 5.")
