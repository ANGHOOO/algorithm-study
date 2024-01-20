n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in arr:
        if x > mid: # 떡의 길이가 절단기 높이보다 길다면
            total += x - mid # total에 남은 떡의 길이만큼 추가

    if total < m: # 만약 남은 떡들의 총 길이가 원하는 길이보다 작다면 높이를 낮춰서 덜 잘라야 한다.
        end = mid - 1

    else: # 만약 남은 떡들의 총 길이가 원하는 길이보다 길다면 높이를 높여서 더 잘라야 한다.
        result = mid
        start = mid + 1

print(result)
        