from functools import reduce

races = [(38,241), (94,1549), (79,1074), (70,1091)]

# part 1
winners=[]
for r in races:
    race_wins=0
    accel = 0
    for i in range(1, r[0]+1):
        if accel * (r[0]+1 - i) > r[1]:
            race_wins += 1
        accel += 1
    winners += [race_wins]

print(f"{reduce(lambda x,y: x*y, winners)=}")

# part 2

accel = 0
race_wins = 0
for i in range(1, 38947971):
    if accel * (38947971 - i) > 241154910741091:
        race_wins += 1
    accel += 1
print(f"{race_wins=}")