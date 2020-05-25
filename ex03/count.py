import string


def text_analyzer(*arg):
    """
This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""
    if (len(arg) > 1):
        print("ERROR")
    elif (len(arg) == 0):
        string2 = input("What is the text to analyse?\n")
        text_analyzer(string2)
    else:
        if isinstance(arg[0], str) is not True:
            print("ERROR")
            return
        ul = 0
        ll = 0
        pm = 0
        sp = 0
        for x in arg[0]:
            if x.isupper():
                ul += 1
            if x.islower():
                ll += 1
            if x in string.punctuation:
                pm += 1
            if x.isspace():
                sp += 1
        print(f"The text contains {len(arg[0])} characters:\n")
        print(f"- {ul} upper letters\n")
        print(f"- {ll} lower letters\n")
        print(f"- {pm} punctuation marks\n")
        print(f"- {sp} spaces")


# text_analyzer("""Python 2.0, released 2000, introduced
# features like List comprehensions and a garbage collection
# system capable of collecting reference cycles.""")
# text_analyzer("""Python is an interpreted, high-level,
# general-purpose programming language. Created by Guido van
# Rossum and first released in 1991, Python's design philosophy
# emphasizes code readability with its notable use of significant
# whitespace.""")
# text_analyzer("qsd", 2)
# print(text_analyzer.__doc__)
# text_analyzer()
