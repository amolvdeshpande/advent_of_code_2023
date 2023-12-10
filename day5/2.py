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


# Fill out gaps in the maps
for i in range(1, 8):
    covered = sorted([(m[2], m[2] + m[3]) for m in maps if m[0] == i])

    print(covered)

    start = 0
    for x in covered:
        if start < x[0]:
            print("adding", i, start, start, x[0] - start)
            maps.append((i, start, start, x[0] - start))
        start = x[1]
    maps.append( (i, start, start, 1000000000000 - start) )

input()

# lets create a queue of things to be expanded
locations = []

queue = [(1, seeds[i], seeds[i]+ seeds[i+1] - 1) for i in range(0, len(seeds), 2)]

# pop from the queue and process
while len(queue) > 0:
    current = queue.pop(0)
    print("---- Processing", current)

    if current[0] == 8:
        # we are done
        locations.append(current)
        continue

    # find all maps that match the current
    for m in maps:
        # m maps a range (m[2], m[2] + m[3]) to (m[1], m[1] + m[3])
        # we are looking to map the range of (current[1], current[2])
        # if m[2] is within the range, then we need to take care of that
        print("checking", m)
        if m[0] == current[0] and current[1] >= m[2] and current[1] <= m[2] + m[3] - 1:
            print("---- Found", m)
            if current[2] <= m[2] + m[3] - 1:
                # the entire range is mapped
                queue.append((current[0] + 1, m[1] + (current[1] - m[2]), m[1] + (current[2] - m[2])))
                print("---- Adding", queue[-1])
            else:
                # only a part of the range is mapped
                queue.append((current[0] + 1, m[1] + (current[1] - m[2]), m[1] + m[3] - 1))
                print("---- Adding", queue[-1])
                # need to handle rest of the range -- append to the beginning
                queue.insert(0, (current[0], m[2] + m[3], current[2]))
                print("---- Adding", queue[0])

print(sorted([l[1] for l in locations]))

#all_break_points = [m[1] for m in maps]
#all_break_points += [m[1] + m[3] for m in maps]
#all_break_points += [m[2] for m in maps]
#all_break_points += [m[2] + m[3] for m in maps]
#all_break_points += [seeds[i] for i in range(0, len(seeds), 2)]
#all_break_points += [seeds[i] + seeds[i+1] for i in range(0, len(seeds), 2)]
#
#all_break_points = sorted(set(all_break_points))
#print(all_break_points)
#
## we will use the index of the start point of a range for the mapping purposes
#def find_index(start):
#    for i in range(len(all_break_points)):
#        if all_break_points[i] == start:
#            return i
#    assert False
#
#
#maps_redone = []
#for m in maps:
#    source_start = m[2]
#    source_end = m[2] + m[3]
#    dest_start = m[1]
#    dest_end = m[1] + m[3]
#
#    for index, bp in enumerate(all_break_points):
#        if bp >= source_start and bp < source_end:
#            print("found", bp, "in", source_start, source_end)
#            print("-- looking for index of", dest_start + (bp - source_start))
#            dest_index = find_index(dest_start + (bp - source_start))
#            maps_redone.append((m[0], index, dest_index))
#
#print(maps_redone)
#
