n, m = map(int, input().split())
arr = []

for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

max_num = 0

for i in range(n):
    temp = min(arr[i])
    if temp > max_num:
        max_num = temp 

print(max_num)
