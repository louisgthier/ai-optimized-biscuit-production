dough_length = 500

biscuits = {
    0: {"length": 4, "value": 6, "defects": {"a": 4, "b": 2, "c": 3}, "id": 0},
    1: {"length": 8, "value": 12, "defects": {"a": 5, "b": 4, "c": 4}, "id": 1},
    2: {"length": 2, "value": 1, "defects": {"a": 1, "b": 2, "c": 1}, "id": 2},
    3: {"length": 5, "value": 8, "defects": {"a": 2, "b": 3, "c": 2}, "id": 3},
}

MAX_BISCUIT_LENGTH = max(b["length"] for b in biscuits.values())

with open("defects.csv") as f:
    lines = f.readlines()
    defects = [line.strip().split(",") for line in lines[1:]]

# Defects never occur at precise integer coordinates, so a defect will never be shared by two tiles.
defect_counts = {}
for x, y in defects:
    x = int(float(x))
    if x not in defect_counts:
        defect_counts[x] = {"a": 0, "b": 0, "c": 0}

    defect_counts[x][y] += 1

for x in range(dough_length):
    if x not in defect_counts:
        defect_counts[x] = {"a": 0, "b": 0, "c": 0}

def check_solution(sol):
    last_position_with_biscuit = -1
    sol = sorted(sol, key=lambda x: x[0])
    value = 0

    valid_sol = []

    is_valid = True

    for i, (x, y) in enumerate(sol):
        biscuit_valid = True

        if x < 0:
            print("Negative x", x, y)
            biscuit_valid = False
        if x + biscuits[y]["length"] > dough_length:
            print("Biscuit too long", x, y)
            biscuit_valid = False
        
        defect_counts_for_biscuit = {"a": 0, "b": 0, "c": 0}
        for j in range(x, x + biscuits[y]["length"]):
            if j in defect_counts:
                for k in defect_counts[j]:
                    defect_counts_for_biscuit[k] += defect_counts[j][k]
        
        if x <= last_position_with_biscuit:
            print("Biscuits overlap", x, y)
            biscuit_valid = False

        for k in defect_counts_for_biscuit:
            if defect_counts_for_biscuit[k] > biscuits[y]["defects"][k]:
                print("Defects don't match", x, y, k, defect_counts_for_biscuit, biscuits[y]["defects"])
                biscuit_valid = False
        
        if biscuit_valid:
            last_position_with_biscuit = x + biscuits[y]["length"] - 1
            value += biscuits[y]["value"]
            valid_sol.append((x, y))
        else:
            is_valid = False

    return value, valid_sol, is_valid



def save_solution(sol, filename):
    with open(filename, "w") as f:
        for x, y in sol:
            f.write("{},{}\n".format(x, y))
        
