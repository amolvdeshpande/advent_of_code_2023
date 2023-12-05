import re

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]


total = 0

num_cards = [1 for i in range(0, 216)]

for index, line in enumerate(lines):
    m = re.match(r'Card\s+\d+: ([\s0-9]+) \| ([\s0-9]+)', line)
    s1 = set([int(x) for x in m.group(1).split()])
    s2 = set([int(x) for x in m.group(2).split()])
    num_matches = len(s1.intersection(s2))

    # increase the num_cards for next num_matches by the count for this card
    print(num_matches)
    for i in range(index+1, index+num_matches+1):
        num_cards[i] += num_cards[index]
    print(num_cards)

for i in range(0, 216):
    total += num_cards[i]
print(total)
