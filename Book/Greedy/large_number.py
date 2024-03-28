n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

# My solution
ans = 0
cnt = 0
sorted_arr = sorted(arr, reverse=True)
for _ in range(m):
    if cnt < k:
        ans += sorted_arr[0]
        cnt += 1
    else:
        ans += sorted_arr[1]
        cnt = 0

print(ans)

# Book Solution    
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first 
        m -= 1
    if m == 0:
        break
    result += second 
    m -= 1

print(result)

