import re

with open('input.txt') as f:
    lines = f.readlines()

directions = lines[0].strip()

steps = {x: (y, z) for l in lines[2:] for x, y, z in re.findall(r'^(\w+) = .(\w+), (\w+).$', l)}

start = 'AAA'

count = 0
while start != 'ZZZ':
    for d in directions:
         start = steps[start][0] if d == 'L' else steps[start][1]
         print("move", "to", start)
         count += 1
         if start == 'ZZZ':
             break
print(count)
