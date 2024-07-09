n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while start <= end:
    mid = (start + end) // 2  # 절단점
    total = 0
    for x in arr:
        if x > mid:
            total += x - mid 
    
    if total < m: # 더 적게 잘렸다면? (절단점 왼쪽으로 옮기기)
        end = mid - 1
    else:
        result = mid 
        start = mid + 1

print(result)
