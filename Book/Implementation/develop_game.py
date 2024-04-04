n, m = map(int, input().split())
x, y, direction = map(int, input().split())
d = [[0] * m for _ in range(n)] # 방문 확인 리스트
d[x][y] = 1

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] # 북, 동, 남, 서

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_count = 0

while True:
    turn_left()
    nx, ny = x + dxs[direction], y + dys[direction]
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny 
        count += 1
        turn_count = 0
        continue
    else:
        turn_count += 1
    
    if turn_count == 4:
        nx, ny = x - dxs[direction], y - dys[direction]
        if arr[nx][ny] == 0:
            x, y = nx, ny 
            turn_count = 0
        else:
            break 

print(count)


