location = 'c2'
arr = [[0] * 8 for _ in range(8)]
loc = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8
}

def cant_go(x, y):
    return x < 1 or y < 1 or x > 8 or y > 8

def moving(location):
    location = list(location)
    x, y = location[1], location[0]
    y, x = loc[y], int(x)
    count = 0

    # case1) 아래로 두 칸, 왼쪽으로 한 칸
    nx, ny = x + 2, y - 1
    if not cant_go(nx, ny):
        count += 1
    # case2) 아래로 두 칸, 오른쪽으로 한 칸
    nx, ny = x + 2, y + 1
    if not cant_go(nx, ny):
        count += 1
    # case3) 위로 두 칸, 왼쪽으로 한 칸
    nx, ny = x - 2, y - 1
    if not cant_go(nx, ny):
        count += 1
    # case4) 위로 두 칸, 오른쪽으로 한 칸
    nx, ny = x - 2, y + 1
    if not cant_go(nx, ny):
        count += 1
    # case5) 왼쪽으로 두 칸, 위로 한 칸
    nx, ny = x - 1, y - 2
    if not cant_go(nx, ny):
        count += 1
    # case6) 왼쪽으로 두 칸, 아래로 한 칸
    nx, ny = x + 1, y - 2
    if not cant_go(nx, ny):
        count += 1
    # case7) 오른쪽으로 두 칸, 위로 한 칸
    nx, ny = y + 2, x - 1
    if not cant_go(nx, ny):
        count += 1
    # case8) 오른쪽으로 두 칸, 아래로 한 칸
    nx, ny = y + 2, x + 1
    if not cant_go(nx, ny):
        count += 1

    return count

print(moving(location))

# 책 풀이
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)