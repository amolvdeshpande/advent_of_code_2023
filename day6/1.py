import math

with open('input.txt') as f:
    lines = f.readlines()

times = [int(x) for x in lines[0].split(":")[1].split()]
distances = [int(x) for x in lines[1].split(":")[1].split()]

def get_max_distance(hold_time, total_time):
    return (total_time - hold_time) * hold_time


print(math.prod([sum([get_max_distance(i, times[j]) > distances[j] for i in range(times[j])]) for j in range(4)]))
