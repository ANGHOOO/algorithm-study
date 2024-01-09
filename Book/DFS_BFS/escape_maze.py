from collections import deque

n, m = 5, 6
arr = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

visited = [[0] * m for _ in range(n)]
count = 0

def bfs(x, y):
    global arr
    q = deque()
    q.append((x, y))
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1

bfs(0, 0)
print(arr[n-1][m-1])
