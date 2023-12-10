import re

with open('input.txt') as f:
    lines = f.readlines()

times = int(lines[0].split(":")[1].replace(" ", ""))
distances = int(lines[1].split(":")[1].replace(r" ", ""))

def get_max_distance(hold_time, total_time):
    return (total_time - hold_time) * hold_time

print(sum([get_max_distance(i, times) > distances for i in range(times)]))
