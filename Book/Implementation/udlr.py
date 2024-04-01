n = int(input())
direction = list(input().split())

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
x, y = 1, 1
mapper = {
    'U' : 0,
    'D' : 1,
    'L' : 2,
    'R' : 3
}

for d in direction:
    dx, dy = dxs[mapper[d]], dys[mapper[d]]
    nx, ny = x + dx, y + dy 
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    else:
        x, y = nx, ny

print(x, y)