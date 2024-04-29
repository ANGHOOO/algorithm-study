# my solution
point = list(input())
x, y = point[0], point[1]
x_mapper = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = x_mapper.index(x)
y = int(y) - 1
answer = 0

def in_range(x, y):
    if x < 0 or y < 0 or x > 7 or y > 7:
        return False
    else:
        return True

# 수평으로 두 칸 이동 후 수직으로 한 칸
# 수직으로 두 칸 이동 후 수평으로 한 칸
dxs, dys = [-2, -2, 2, 2, -1, 1, -1, 1], [-1, 1, -1, 1, -2, -2, 2, 2]

for dx, dy in zip(dxs, dys):
    nx, ny = x + dx, y + dy 
    if in_range(nx, ny):
        answer += 1

print(answer)
    
# book solution
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)