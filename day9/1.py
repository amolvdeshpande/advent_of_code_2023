import math

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    sequences = [[int(x) for x in l.split()] for l in lines]

def find_next(sequence):
    if all([x == 0 for x in sequence]):
        return 0
    else:
        n = find_next([sequence[i] - sequence[i-1] for i in range(1, len(sequence))])
        return sequence[-1] + n

print(sum([find_next(sequence) for sequence in sequences]))
