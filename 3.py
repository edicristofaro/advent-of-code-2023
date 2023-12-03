import itertools

from math import prod

with open("input3.txt") as f:
    lines = f.read().splitlines()

def check_neighbors(y, x):
    offsets = [(0,1), (1,0), (-1,0), (0,-1), (1, 1), (-1,-1), (1,-1), (-1, 1)]
    for o in offsets:
        ox = x + o[0]
        oy = y + o[1]
        gear_symbol_coords = None
        try:
            if (not lines[ox][oy].isdigit()) and (not lines[ox][oy] == "."):
                if lines[ox][oy] == "*":
                    gear_symbol_coords = (ox, oy)
                return True, gear_symbol_coords
        except Exception as e:
            pass
    return False, None

part_numbers = []
part_numbers_with_gear_coords = {}
for i, l in enumerate(lines):
    is_part_number = False
    gear_symbol_coords = None
    part_check = False
    gear_symbol_check = None
    accum = ""
    for j, p in enumerate(l):
        if p.isdigit():
            accum += p
            part_check, gear_symbol_check = check_neighbors(j, i)
            if part_check:
                is_part_number = True
            if gear_symbol_check is not None:
                gear_symbol_coords = gear_symbol_check
        if (not p.isdigit()) or j == len(l)-1:
            if len(accum) > 0 and is_part_number:
                part_numbers.append(int(accum))
                if gear_symbol_coords is not None:
                    if gear_symbol_coords in part_numbers_with_gear_coords.keys():
                        part_numbers_with_gear_coords[gear_symbol_coords].append(int(accum))
                    else:
                        part_numbers_with_gear_coords[gear_symbol_coords] = [int(accum)]
            accum = ""
            is_part_number = False
            part_check = False
            gear_symbol_coords = None
            gear_symbol_check = None

# part 1
print(f"{sum(part_numbers)=}") 

# part 2
print(f"{sum(prod(v) for v in part_numbers_with_gear_coords.values() if len(v) == 2)=}")

            