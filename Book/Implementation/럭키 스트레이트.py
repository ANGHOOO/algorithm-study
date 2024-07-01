arr = list(map(int, input()))
length = len(arr)
criterion = length // 2

left = arr[:criterion]
right = arr[criterion:]

left_sum = sum(left)
right_sum = sum(right)

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')
