import re

sum = 0

def get_color(s, color):
    m = re.match(r'([0-9]*) (.*)', s)
    if m.group(2) == color:
        return int(m.group(1))
    else:
        return 0

with open('input.txt') as f:
    for line in f:
        line = line.strip()

        m =  re.match(r'Game ([0-9]*): (.*)$', line)
        i = m.group(1)

        possible = True

        m = re.split(r'[,;] ', m.group(2))

        p = max([get_color(x, 'blue') for x in m]) * max([get_color(x, 'green') for x in m]) * max([get_color(x, 'red') for x in m])

        sum += p

        print(m)
print(sum)
