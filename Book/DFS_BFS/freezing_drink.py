n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

count = 0

def dfs(arr, i, j):
    global count 

    if i < 0 or i >= n or j < 0 or j >= m or arr[i][j] == 1:
        return 
    else:
        arr[i][j] = 1
        dfs(arr, i+1, j)
        dfs(arr, i-1, j)
        dfs(arr, i, j+1)
        dfs(arr, i, j-1)


for i in range(n):
    for j in range(m):
        if arr[i][j] != 1:
            dfs(arr, i, j)
            count += 1

print(count)