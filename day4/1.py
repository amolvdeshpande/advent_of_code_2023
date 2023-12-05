import re

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]


total = 0

for line in lines:
    m = re.match(r'Card\s+\d+: ([\s0-9]+) \| ([\s0-9]+)', line)
    s1 = set([int(x) for x in m.group(1).split()])
    s2 = set([int(x) for x in m.group(2).split()])
    if len(s1.intersection(s2)) > 0:
        total += pow(2, len(s1.intersection(s2))-1)
print(total)
