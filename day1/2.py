import re

sum = 0

def find_first_digit(s):
    if s[0].isdigit():
        return s[0]
    for (x, y) in [('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)]:
        if s.startswith(x):
            return str(y)
    return find_first_digit(s[1:])

def find_last_digit(s):
    if s[-1].isdigit():
        return s[-1]
    for (x, y) in [('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)]:
        if s.endswith(x):
            return str(y)
    return find_last_digit(s[:-1])


with open('input.txt', 'r') as f:
    for l in f:
        l = l.strip()
        ls = find_first_digit(l) + find_last_digit(l)
        sum = sum + int(ls)
print(sum)
