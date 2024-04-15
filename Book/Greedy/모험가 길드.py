arr = list(map(int, input().split()))

arr.sort()
result = 0
fear = 0
fear_count = 0

for i in range(len(arr)):
    fear = arr[i]
    fear_count += 1
    if fear_count == fear:
        result += 1
        fear_count = 0

print(result)    