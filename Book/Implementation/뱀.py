n = int(input()) # 격자 크기
k = int(input()) # 사과의 개수
data = [[0] * (n+1) for _ in range(n+1)]
for _ in range(k):
    x, y = map(int, input().split())
    data[x][y] = 1

l = int(input()) # 방향 변환 횟수
info = []
for _ in range(l):
    time, direction = input().split()
    info.append((int(time), direction))

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동, 남, 서, 북

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction 

def simulate():
    x, y = 1, 1 # 뱀의 처음 좌표
    data[x][y] = 2
    time = 0
    index = 0
    direction = 0
    q = [(x, y)]

    while True:
        nx, ny = x + dx[direction], y + dy[direction]
        # 갈 수 있는 경우
        if nx >= 1 and nx <= n and ny >= 1 and ny <= n and data[nx][ny] != 2:
            # 사과가 없는 경우
            if data[nx][ny] == 0:
                q.append((nx, ny))
                data[nx][ny] = 2
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있는 경우
            if data[nx][ny] == 1:
                q.append((nx, ny))
                data[nx][ny] = 2
        # 갈 수 없는 경우
        else:
            time += 1
            break 
        x, y = nx, ny 
        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1

    return time 

print(simulate())