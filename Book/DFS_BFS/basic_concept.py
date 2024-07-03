# DFS (Depth First Search)
# 스택 자료구조를 사용 -> 재귀함수를 통해 구현하면 편리
# <DFS의 동작 과정>
# 1. 시작 노드를 스택에 넣고 방문처리. (방문처리를 하는 이유는 이미 방문한 노드를 다시 탐색하지 않아 효율성을 높이기 위함)
# 2. 스택에 쌓인 노드와 인접한 노드 중 방문하지 않은 노드가 있다면 스택에 넣고 방문처리. (이때 방문하지 않은 인접한 노드가 여러개 있다면 숫자가 낮은 노드를 먼저 넣는것이 관례.)
# 3. 방문하지 않은 노드가 없을때까지 1, 2번 과정을 반복 수행

def dfs(graph, v, visited):
    visited[v] = True 
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8], # 1번 노드
    [1, 7], # 2번 노드
    [1, 4, 5], # 3번 노드
    [3, 5], # 4번 노드
    [3, 4], # 5번 노드
    [7], # 6번 노드
    [2, 6, 8], # 7번 노드
    [1, 7] # 8번 노드
]

visited = [False] * 9
dfs(graph, 1, visited) # 1->2->7->6->8->3->4->5

# BFS(Breadth First Search) : 너비 우선 탐색
# 재귀 함수를 통해 구현하는 DFS에 비해 일반적으로 실행 시간이 더 빠름

# BFS의 동작 방식
# 1. 시작 노드를 큐에 삽입하고 방문 처리
# 2. 큐에 삽입된 노드를 꺼내서 해당 노드와 인접 한 노드 중 방문하지 않은 노드 모두를 큐에 삽입하고 방문 처리
# 3. 큐가 빌때까지 2번의 과정을 반복 수행
from collections import deque 

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True 

    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True 

graph = [
    [],
    [2, 3, 8], # 1번 노드
    [1, 7], # 2번 노드
    [1, 4, 5], # 3번 노드
    [3, 5], # 4번 노드
    [3, 4], # 5번 노드
    [7], # 6번 노드
    [2, 6, 8], # 7번 노드
    [1, 7] # 8번 노드
]

visited = [False] * 9
bfs(graph, 1, visited) # 1 -> 2 -> 3 -> 8 -> 7 -> 4 -> 5 -> 6