arr = list(map(int, input()))
length = len(arr)

if sum(arr[:length // 2]) == sum(arr[length // 2:]):
    print('LUCKY')
else:
    print('READY')