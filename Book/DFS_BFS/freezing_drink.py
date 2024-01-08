from collections import deque

n, m = 4, 5
graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    
    return False

result = 0
for i in range(n+1):
    for j in range(m+1):
        if dfs(i, j) == True:
            result += 1

print(result)
