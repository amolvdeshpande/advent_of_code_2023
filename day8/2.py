import re
import math

with open('input.txt') as f:
    lines = f.readlines()

directions = lines[0].strip()

steps = {x: (y, z) for l in lines[2:] for x, y, z in re.findall(r'^(\w+) = .(\w+), (\w+).$', l)}

## find the path lengths for each start node, and do an LCM
starts = [x for x in steps if x[2] == 'A']
ends = [x for x in steps if x[2] == 'Z']

def find_path_length(start, end):
    count = 0
    visited = set()
    while start != end:
        for index, d in enumerate(directions):
             start = steps[start][0] if d == 'L' else steps[start][1]
             count += 1
             if start == end:
                return count
             if (start, index+1) in visited:
                return -1
             visited.add((start, index+1))
    assert False

# cheat --  use the fact that there is only one path for each start -- otherwise need to check for all combinations
all_path_lengths = [find_path_length(s, e) for s in starts for e in ends]
print(math.lcm(*[l for l in all_path_lengths if l != -1]))
