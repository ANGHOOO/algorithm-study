arr = list(input())
start = arr[0]
count = 0

for i in range(1, len(arr)):
    if arr[i] != start:
        start = arr[i]
        count += 1

print(count - 1)