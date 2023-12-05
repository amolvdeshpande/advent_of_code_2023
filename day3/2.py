import re

with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

d = {}

def look_for_star(index, start, end, number):
    for i in range(max(0, start-1), min(end+1, len(lines[index]))):
        if lines[index][i] == '*':
           d.setdefault((index, i), []).append(number)

for index, line in enumerate(lines):
    if index > 0: print(lines[index-1])
    print(line)
    if index < len(lines) - 1: print(lines[index+1])

    for match in re.finditer(r'(\d+)', line):
        start, end, number = match.start(), match.end(), match.group(0)

        look_for_star(index, start, end, number)
        if index > 0:
            look_for_star(index-1, start, end, number)
        if index < len(lines) - 1:
            look_for_star(index+1, start, end, number)


print(sum([int(d[key][0]) * int(d[key][1]) for key in d if len(d[key]) == 2]))
