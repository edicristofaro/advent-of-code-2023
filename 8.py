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
steps = 0 
dests = ['AAA', 'MTA', 'QNA']
z_dests = ['ZZZ', 'BLZ', 'NPZ']

while set(dests) != set(z_dests):
    for d in directions:
        temp_dests = []
        # print(f"Start Dests: {dests}\n{d=}")
        for dest in dests:
            temp_dests.append(nodes.get(dest)[d])
        steps += 1
        dests = temp_dests[:]
        # print(f"End Dests: {dests}\n{steps=}")
        if len(set([i[2] for i in dests])) == 1 and dests[0][2] == "Z":
            print(dests)
            print(f"Out! Part 2: {steps=}")
            sys.exit()

print(f"Part 2: {steps=}")