import re

with open("input.txt") as f:
    lines = f.readlines()


seeds = [int(x) for x in lines[0].split(":")[1].split()]

maps = []

current = 0
for line in lines[1:]:
    if re.match(r"seed-to-soil", line):
        current = 1 # "s-to-s"
    elif re.match(r"soil-to-fertilizer", line):
        current = 2 # "s-to-f"
    elif re.match(r"fertilizer-to-water", line):
        current = 3 # "f-to-w"
    elif re.match(r"water-to-light", line):
        current = 4 # "w-to-l"
    elif re.match(r"light-to-temperature", line):
        current = 5 # "l-to-t"
    elif re.match(r"temperature-to-humidity", line):
        current = 6 # "t-to-h"
    elif re.match(r"humidity-to-location", line):
        current = 7 # "h-to-l"
    elif len(line) == 1:
        continue
    else: 
        maps.append((current, int(line.split()[0]), int(line.split()[1]), int(line.split()[2])))


def find_next_hop(current, source_number, maps):
    for m in maps:
        if m[0] == current and source_number >= m[2] and source_number < m[2] + m[3]:
            return m[1] - m[2] + source_number
    return source_number

for seed in seeds:
    print("-----------")
    next_hop = seed
    for i in range(1, 8):
        next_hop = find_next_hop(i, next_hop, maps)
    print(next_hop)

