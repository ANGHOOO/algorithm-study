def binary_search(array, target, start, end):
    if start > end:
        return None 
    
    mid = (start + end) // 2 

    if array[mid] == target:
        return mid 
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    
    else:
        return binary_search(array, target, mid+1, end)
    
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

for t in targets:
    if binary_search(arr, t, 0, n-1) == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')