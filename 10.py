with open("input10.txt") as f:
    lines = f.read().splitlines()

grid = {}
connections = {
    "|": [(0, 1), (0, -1)],
    "-": [(1, 0), (-1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, 1), (-1, 0)],
    "F": [(0, 1), (1, 0)],
}
for y, l in enumerate(lines):
    for x, m in enumerate(l):
        if m != ".":
            grid[(x, y)] = m


def makes_connection(point, neighbor):
    valid_connections_p = connections[grid[point]]  # returns the valid offsets

    # handle non-existent points
    neighbor_point = grid.get(neighbor, None)
    if neighbor_point is None:
        return False
    valid_connections_n = connections[neighbor_point]

    # adjust the point and the neighbor by the offsets, get the coordinates
    valid_coords_p = []
    for p in valid_connections_p:
        valid_coords_p.append(tuple([point[0] + p[0], point[1] + p[1]]))

    valid_coords_n = []
    for p in valid_connections_n:
        valid_coords_n.append(tuple([neighbor[0] + p[0], neighbor[1] + p[1]]))

    if point in valid_coords_n and neighbor in valid_coords_p:
        return True
    return False


def get_neighbors(point):
    return [
        tuple([point[0] + 1, point[1]]),
        tuple([point[0] - 1, point[1]]),
        tuple([point[0], point[1] + 1]),
        tuple([point[0], point[1] - 1]),
    ]


def move(loc, visited):
    possible_points = get_neighbors(loc)
    possible_points = [p for p in possible_points if p not in visited]

    for p in possible_points:
        if makes_connection(loc, p):
            visited.append(p)
            return p, visited


# part 1
start_point = (14, 111)
loc_a = (14, 110)  # don't deal with the S point, just pick the two starting points
loc_b = (15, 111)

# start_point = (1, 1)
# loc_a = (1, 2)  # don't deal with the S point, just pick the two starting points
# loc_b = (2, 1)

steps = 1
visited_a = [start_point, loc_a]  # put the S point here
visited_b = [start_point, loc_b]

while loc_a != loc_b:
    loc_a, visited_a = move(loc_a, visited_a)
    loc_b, visited_b = move(loc_b, visited_b)
    steps += 1

print(f"{steps=}")


# part 2
def is_contained(point, loop, grid_width):
    if point in loop:
        return False

    intersect_count = 0
    for i in range(point[0], grid_width):
        if (i, point[1]) in loop and grid[(i, point[1])] not in ("F", "-", "7"):
            intersect_count += 1

    if intersect_count % 2 == 0:
        return False
    else:
        return True


loop = visited_a + visited_b

contained_count = 0
for y in range(0, len(lines)):
    for x in range(0, len(lines)):
        if (x, y) not in loop:
            contained_count += 1 if is_contained((x, y), loop, len(lines)) else 0
print(f"{contained_count=}")
