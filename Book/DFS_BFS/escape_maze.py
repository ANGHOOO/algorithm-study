from collections import deque 

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy 
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue 
            if arr[nx][ny] == 0:
                continue 
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1 
                q.append((nx, ny))

bfs(0, 0)

print(arr[n-1][m-1])