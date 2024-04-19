n = int(input())
arr = list(map(int, input().split()))

target = 1
arr.sort()

for x in arr:
    if target < x:
        break 
    else: 
        target += x 

print(target)