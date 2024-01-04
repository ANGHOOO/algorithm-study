n, m, k = map(int, input().split())
arr = list(map(int, input()) for _ in range(n))

# n, m, k = 5, 8, 3
# arr = [2, 4, 5, 4, 6]

arr.sort()
first = arr[-1]
second = arr[-2]

answer = 0
cnt = 0

for i in range(m):
    if i == 0:
        answer += first
        cnt += 1
        continue

    if cnt % k == 0:
        answer += second
    else:
        answer += first
    cnt += 1

print(answer)