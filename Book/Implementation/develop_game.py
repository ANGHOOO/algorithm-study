# n, m = 4, 4
# x, y, direction = 1, 1, 0
# visited = [[0] * m for _ in range(n)]
# visited[x][y] = 1 # 현재 좌표 방문 처리
# arr = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]

n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())

arr = []
for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북, 동, 서, 남

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx, ny = x + dx[direction], y + dy[direction]

    if visited[nx][ny] == 0 and arr[nx][ny] == 0:
        visited[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx, ny = x - dx[direction], y - dy[direction]
        if arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            break

        turn_time = 0

print(count)