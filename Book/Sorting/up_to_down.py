# n = int(input())
# arr = list(map(int, input()) for _ in range(n))

n = 3
arr = [15, 27, 12]
sorted_arr = sorted(arr, reverse=True)

for num in sorted_arr:
    print(num, end=' ')