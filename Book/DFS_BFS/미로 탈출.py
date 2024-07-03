from collections import deque 
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(x, y):
    q = deque()
    q.append((x, y))
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy 
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue 

            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1 

bfs(0, 0)
answer = graph[n-1][m-1]
print(answer)