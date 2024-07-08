def binary_search(array, target, start, end):
    if start > end:
        return None 
    
    mid = (start + end) // 2 

    if array[mid] == target:
        return mid 
    
    elif array[mid] > target: # 왼쪽 탐색
        return binary_search(array, target, start, mid-1)
    
    else: # 오른쪽 탐색
        return binary_search(array, target, mid+1, end)
    