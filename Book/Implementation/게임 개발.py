n, m = map(int, input().split())
x, y, direction = map(int, input().split())
d = [[0] * m for _ in range(n)]
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

count = 1
turn_time = 0
d[x][y] = 1

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

while True:
    turn_left()
    nx, ny = x + dx[direction], y + dy[direction]

    # 시계 반대 방향으로 돌리고 이동할 수 있다면
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        count += 1
        x, y = nx, ny 
        d[x][y] = 1
        turn_time = 0
        continue
    # 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로만 회전 수행
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