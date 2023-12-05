import re

sum = 0

with open('input.txt') as f:
    for line in f:
        line = line.strip()

        m =  re.match(r'Game ([0-9]*): (.*)$', line)
        i = m.group(1)

        possible = True

        print(m.group(2).split("; "))
        for x in m.group(2).split("; "):
            for y in x.split(", "):
                mm = re.match(r'([0-9]*) (.*)', y)
                print(mm.group(1))
                if ( (mm.group(2) == 'green' and int(mm.group(1)) > 13) or
                     (mm.group(2) == 'red' and int(mm.group(1)) > 12) or
                     (mm.group(2) == 'blue' and int(mm.group(1)) > 14) ):
                    possible = False
        if possible:
            sum += int(i)
print(sum)
