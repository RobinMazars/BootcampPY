import sys
list = []
for value in sys.argv[1:]:
    value = ''.join(reversed(value))
    list.append(value.swapcase())

list = reversed(list)
print(*list, end="")
