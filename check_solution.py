
def check_solution(sol):
    value = 0
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
        
        if i != 0 and x <= sol[i - 1][0] + biscuits[sol[i - 1][1]]["length"] - 1:
            print("Biscuits overlap", x, y)
            biscuit_valid = False

        for k in defect_counts_for_biscuit:
            if defect_counts_for_biscuit[k] > biscuits[y]["defects"][k]:
                print("Defects don't match", x, y, k, defect_counts_for_biscuit, biscuits[y]["defects"])
                biscuit_valid = False

        if biscuit_valid:
            value += biscuits[y]["value"]

    return value
