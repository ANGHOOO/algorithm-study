def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid 
        elif array[mid] > target: # 왼쪽을 탐색
            end = mid - 1 
        else: # 오른쪽을 탐색
            start = mid + 1
    
    return None 