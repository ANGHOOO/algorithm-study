# 1. 빈칸이 0인 좌표 중 벽을 세울 3개를 고르기
# 2. 고른 3개의 좌표 값을 0으로 바꾸기
# 3. 바이러스를 상하좌우로 퍼뜨리기
# 4. 감염 안 된 구역 갯수 세기
# 5. 벽 세웠던 좌표 다시 되돌리기
from itertools import combinations 
from collections import deque 

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

org_graph = []
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(graph[i][j])
    org_graph.append(temp)

# 0인 좌표 찾기
zero_coord = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_coord.append((i, j))

# 빈칸이 0인 좌표 중 벽을 세울 3개를 고르기
zero_comb = list(combinations(zero_coord, 3))

def bfs():
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append((i, j))

    visited = [[0] * m for _ in range(n)]
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy 
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue 
            
            if visited[nx][ny]:
                continue 

            if graph[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
                graph[nx][ny] = 2

def count_zero():
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1

    return count 

def simulate():
    global graph 
    answer = 0
    # 0인 좌표 3개를 골라서 벽 세우기
    for comb in zero_comb:
        graph = [row[:] for row in org_graph]
        for a, b in comb:
            graph[a][b] = 1
        # 바이러스 퍼뜨리기
        bfs()
        # 0인 갯수 세기
        result = count_zero()
        answer = max(answer, result)
        
    return answer 

answer = simulate()
print(answer)