from collections import OrderedDict

# part 1

with open("input1.txt") as f:
    lines = f.read().splitlines()

numbers = []

for l in lines.copy():
    l = [c for c in l if c.isdigit()]
    if len(l) > 0:
        numbers.append(int(l[0] + l[-1]))

print(sum(numbers))

# part 2

# need to account for numbers with overlapping first and last letters, when the larger number comes before the smaller
# there's probably a more clever way to do this
digits = OrderedDict({"twone": 21, "oneight": 18, "eightwo": 82, "one": 1, "two": 2, "three":3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9})

numbers2 = []

for l in lines.copy():
    for k in digits.keys():
        l = l.replace(k, str(digits[k]))
    l = [c for c in l if c.isdigit()]
    if len(l) > 0:
        numbers2.append(int(l[0] + l[-1]))

print(sum(numbers2))