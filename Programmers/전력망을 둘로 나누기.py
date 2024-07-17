from collections import deque

def solution(n, wires):
    answer = float('inf')
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        def bfs(start):
            q = deque([start])
            visited = [0] * (n+1)
            visited[start] = 1
            cnt = 1
            
            while q:
                x = q.popleft()
                for v in graph[x]:
                    if not visited[v]:
                        q.append(v)
                        visited[v] = 1
                        cnt += 1
                        
            return cnt
        
        answer = min(abs(bfs(a) - bfs(b)), answer)
        
        graph[a].append(b)
        graph[b].append(a)
        
    return answer