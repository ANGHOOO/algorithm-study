arr = list(input())

result = int(arr[0])
for i in range(1, len(arr)):
    if result < 2 or int(arr[i]) < 2:
        result += int(arr[i])
    else:
        result *= int(arr[i])

print(result)