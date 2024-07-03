from collections import deque 

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited):
    q = deque()
    q.append(start)
    visited[start] = True
    dist = 1 
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                distance[i] = distance[v] + 1

bfs(graph, x, visited)

result = []
for i in range(len(distance)):
    if distance[i] == k:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    for num in result:
        print(num)