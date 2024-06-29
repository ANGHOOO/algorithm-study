# 1 5 4 3 2 4 5 2

# 1 : 1
# 2 : 2
# 3 : 1
# 4 : 2
# 5 : 2

# 7 + (2 * 5) + (1 * 4) + (2 * 2)

n, m = map(int, input().split())
weight = list(map(int, input().split()))

arr = [0] * 11

for w in weight:
    arr[w] += 1

result = 0
for i in range(1, 11):
    result += arr[i] * (n - arr[i])
    n -= arr[i]

print(result)