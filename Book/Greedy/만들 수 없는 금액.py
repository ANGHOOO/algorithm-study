n = int(input())
arr = list(map(int, input().split()))

arr.sort()

target = 1
for num in arr:
    if num > target:
        break 
    else:
        target += num 

print(target)