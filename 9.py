with open("input9.txt") as f:
    lines = f.read().splitlines()

lines = [l.split() for l in lines]
histories = []

for l in lines:
    histories.append([int(i) for i in l])

# part 1
extrapolated_values = []

for hist in histories:
    diff_tree = []
    def pair_differences(hist):
        diffs = []
        for i, j in enumerate(hist[1:]):
            diffs.append(j - hist[i])
        if diffs:
            pair_differences(diffs)
            diff_tree.append(diffs)
        return(diffs)

    pair_differences(hist)
    diff_tree.append(hist)


    extrapolated_value = [0]
    for d in diff_tree:
        extrapolated_value.append(extrapolated_value[-1] + d[-1])

    extrapolated_values.append(extrapolated_value[-1])

print(sum(extrapolated_values))

# part 2

extrapolated_values = []

for hist in histories:
    diff_tree = []
    def pair_differences(hist):
        diffs = []
        for i, j in enumerate(hist[1:]):
            diffs.append(j - hist[i])
        if diffs:
            pair_differences(diffs)
            diff_tree.append(diffs)
        return(diffs)

    pair_differences(hist)
    diff_tree.append(hist)


    extrapolated_value = [0]
    for d in diff_tree:
        extrapolated_value.append(d[0] - extrapolated_value[-1])

    extrapolated_values.append(extrapolated_value[-1])

print(sum(extrapolated_values))