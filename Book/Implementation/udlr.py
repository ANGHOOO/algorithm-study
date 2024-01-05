N = 5
direction = ['R', 'R', 'R', 'U', 'D', 'D']
start_x, start_y = 1, 1

dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

mapper = {
    'L' : 0,
    'R' : 1,
    'U' : 2,
    'D' : 3
}

for direc in direction:
    d = mapper[direc]
    dx, dy = dxs[d], dys[d]
    new_x, new_y = start_x + dx, start_y + dy

    if new_x < 1 or new_x > N or new_y < 1 or new_y > N:
        continue

    start_x, start_y = new_x, new_y

print(start_x, start_y)