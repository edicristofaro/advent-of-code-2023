# part 1

with open("input2.txt") as f:
    lines = f.read().splitlines()

maxcubes = {"red": 12, "blue": 14, "green": 13}

possible_games = []

game_id = 1
for l in lines.copy():
    l = l.replace(": ", ":")
    l = l.replace("; ", ";")
    l = l.replace(", ", ",")
    subsets = l.split(":")[1] # take everything after the game id
    red, green, blue = 0, 0, 0
    for subset in subsets.split(";"): # split by each shown subset
        for s in subset.split(","): # take each quantity-color pair in the subset
            pair = s.split(" ")
            pair[0] = int(pair[0])
            if pair[1] == 'red' and pair[0] > red:
                red = int(pair[0])
            if pair[1] == 'green' and pair[0] > green:
                green = int(pair[0])
            if pair[1] == 'blue' and pair[0] > blue:
                blue = int(pair[0])
    if red <= maxcubes["red"] and blue <= maxcubes["blue"] and green <= maxcubes["green"]:
        possible_games.append(game_id)
    game_id += 1

print(sum(possible_games))

# part 2

game_powers = []

for l in lines.copy():
    l = l.replace(": ", ":")
    l = l.replace("; ", ";")
    l = l.replace(", ", ",")
    subsets = l.split(":")[1] # take everything after the game id
    red, green, blue = 0, 0, 0
    for subset in subsets.split(";"): # split by each shown subset
        for s in subset.split(","): # take each quantity-color pair in the subset
            pair = s.split(" ")
            pair[0] = int(pair[0])
            if pair[1] == 'red' and pair[0] > red:
                red = int(pair[0])
            if pair[1] == 'green' and pair[0] > green:
                green = int(pair[0])
            if pair[1] == 'blue' and pair[0] > blue:
                blue = int(pair[0])
    game_powers.append(red * green * blue)

print(sum(game_powers))

# combined

possible_games = []
game_powers = []

game_id = 1
for l in lines.copy():
    l = l.replace(": ", ":")
    l = l.replace("; ", ";")
    l = l.replace(", ", ",")
    subsets = l.split(":")[1] # take everything after the game id
    red, green, blue = 0, 0, 0
    for subset in subsets.split(";"): # split by each shown subset
        for s in subset.split(","): # take each quantity-color pair in the subset
            pair = s.split(" ")
            pair[0] = int(pair[0])
            if pair[1] == 'red' and pair[0] > red:
                red = int(pair[0])
            if pair[1] == 'green' and pair[0] > green:
                green = int(pair[0])
            if pair[1] == 'blue' and pair[0] > blue:
                blue = int(pair[0])
    game_powers.append(red * green * blue)
    if red <= maxcubes["red"] and blue <= maxcubes["blue"] and green <= maxcubes["green"]:
        possible_games.append(game_id)
    game_id += 1

print(f"{sum(possible_games)=}")
print(f"{sum(game_powers)=}")