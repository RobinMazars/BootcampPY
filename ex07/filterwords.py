import sys
import string
if (len(sys.argv) == 3):
    try:
        s = sys.argv[1]
        if s.isdigit() is True:
            print("ERROR")
        else:
            n = int(sys.argv[2])
            for i in string.punctuation:
                s = s.replace(i, '')
            list = s.split(" ")
            # print(list)
            list2 = []
            for w in list:
                if len(w) > n:
                    list2.append(w)
            list = list2
            print(list)

    except ValueError:
        print("ERROR")
else:
    print("ERROR")
