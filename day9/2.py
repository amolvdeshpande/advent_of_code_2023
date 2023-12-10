import math

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    sequences = [[int(x) for x in l.split()] for l in lines]

print(sequences)

def find_prev(sequence):
    if all([x == 0 for x in sequence]):
        return 0
    else:
        n = find_prev([sequence[i] - sequence[i-1] for i in range(1, len(sequence))])
        return sequence[0] - n

print(sum([find_prev(sequence) for sequence in sequences]))
