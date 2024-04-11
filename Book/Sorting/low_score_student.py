n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input().split()))

arr.sort(key=lambda x : int(x[1]))

for name, score in arr:
    print(name, end=' ')
