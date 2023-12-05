import re

with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

total = 0

def is_symbol(c):
    return c not in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def check_for_symbol(line, start, end):
    return any([is_symbol(line[i]) for i in range(max(0, start-1), min(len(line), end+1))])

for index, line in enumerate(lines):
    for match in re.finditer(r'(\d+)', line):
        start, end, number = match.start(), match.end(), match.group(0)

        # need to look for a symbol in start-1 or end+1
        found_symbol = False
        if check_for_symbol(line, start, end) or (index > 0 and check_for_symbol(lines[index-1], start, end)) or (index < len(lines) - 1 and check_for_symbol(lines[index+1], start, end)):
               print(number)
               total += int(number)

#print(total)
