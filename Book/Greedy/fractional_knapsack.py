cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2)
]

def fractional_knapsack(carge):
    capacity = 15
    pack = []
    result = 0
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)

    for p in pack:
        if capacity - p[2] >= 0:
            result += p[1]
            capacity -= p[2]
        else:
            fraction = capacity / p[2]
            result += p[1] * fraction 
            break 

    return result 

r = fractional_knapsack(cargo)
print(r)
