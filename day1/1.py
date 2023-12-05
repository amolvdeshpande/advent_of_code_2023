import re

s = 0

with open('input.txt', 'r') as f:
    for l in f:
        l = re.sub(r'[^0-9]*', '', l.strip())
        ls = list(l)[0] + list(l)[-1]
        s = s + int(ls)
print(s)

#print(sum([int(re.sub(r'[^0-9]*', '', l.strip())[0] + re.sub(r'[^0-9]*', '', l.strip())[-1]) for l in f]))
