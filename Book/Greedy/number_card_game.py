# 나의 답안 --> 2중 반복문을 사용하여 최소값을 배열에 저장한 뒤 마지막에 해당 배열에서 최대값 찾기
n, m = 2, 4
arr = [[7, 3, 1, 8], [3, 3, 3, 4]]

answer = []

for i in range(n):
    min_num = float('inf')
    for j in range(m):
        min_num = min(min_num, arr[i][j])
    answer.append(min_num)

print(max(answer))
    
# 책의 답안 --> 하나의 반복문을 사용하여 최소값과 최대값을 같이 업데이트
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)
    