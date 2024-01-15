# n = int(input())
# arr = [list(input()) for _ in range(n)]

n = 2
arr = [('홍길동', 95), ('이순신', 77), ('이영훈', 100)]

sorted_arr = sorted(arr, key=(lambda x : x[1]))

for name, score in sorted_arr:
    print(name, end = ' ')