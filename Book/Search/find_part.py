n = int(input())
parts = list(map(int, input().split()))
m = int(input())
finds = list(map(int, input().split()))

parts.sort()
finds.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return 'yes'
        
        elif array[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1

    return 'no'

for part in finds:
    answer = binary_search(parts, part, 0, n-1)
    print(answer, end=' ')
    