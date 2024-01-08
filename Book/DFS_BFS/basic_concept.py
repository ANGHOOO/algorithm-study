def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8], # 1번 노드와 연결된 노드
    [1, 7], # 2번 노드와 연결된 노드
    [1, 4, 5], # 3번 노드와 연결된 노드
    [3, 5], # 4번 노드와 연결된 노드
    [3, 4], # 5번 노드와 연결된 노드
    [7], # 6번 노드와 연결된 노드
    [2, 6, 8], # 7번 노드와 연결된 노드
    [1, 7] # 8번 노드와 연결된 노드
]

visited = [False] * 9
dfs(graph, 1, visited)
print()

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8], # 1번 노드와 연결된 노드
    [1, 7], # 2번 노드와 연결된 노드
    [1, 4, 5], # 3번 노드와 연결된 노드
    [3, 5], # 4번 노드와 연결된 노드
    [3, 4], # 5번 노드와 연결된 노드
    [7], # 6번 노드와 연결된 노드
    [2, 6, 8], # 7번 노드와 연결된 노드
    [1, 7] # 8번 노드와 연결된 노드
]

visited = [False] * 9
bfs(graph, 1, visited)