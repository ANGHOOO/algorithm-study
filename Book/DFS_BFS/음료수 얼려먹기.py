# DFS 풀이
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False 
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        bfs(x-1, y)
        bfs(x+1, y)
        bfs(x, y-1)
        bfs(x, y+1)
        return True 
    return False 

result = 0
for i in range(n):
    for j in range(m):
        if bfs(i, j):
            result += 1

print(result)