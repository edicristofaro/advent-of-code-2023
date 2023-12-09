import sys

with open("input8.txt") as f:
    lines = f.read().splitlines()

directions = lines[0]
directions = [int(d.replace("L","0").replace("R","1")) for d in directions]

nodes = {}
for l in lines[2:]:
    nodes[l.split(" = ")[0]] = l.split(" = ")[1][1:4], l.split(" = ")[1][6:9]


# part 1
dest = 'AAA'
steps = 0

while dest != 'ZZZ':
    for d in directions:
        dest = nodes.get(dest)[d]
        steps += 1
        if dest == 'ZZZ':
            break

# 14681
print(f"Part 1: {steps=}")

# part 2
dests = [n for n in nodes.keys() if n[-1] == "A"]
a_dests = [n for n in nodes.keys() if n[-1] == "A"]
z_dests = [n for n in nodes.keys() if n[-1] == "Z"]
print(f"{dests=}\n{z_dests=}")
paths = []

for i, dest in enumerate(dests):
    start_dest = dest
    steps = 0
    while dest[-1] != 'Z':
        for d in directions:
            dest = nodes.get(dest)[d]
            steps += 1
            if dest[-1] == 'Z':
                print(f"Part 2: {start_dest=} {dest=} {steps=}")
                paths.append(steps)
                break

# I'm not entirely sure why this works - probably only does if each starting point has only one path to a destination, or its luck
from math import lcm
print(lcm(*paths))