import sys
input = sys.stdin.readline

N = int(input())
rank = [int(input()) for _ in range(N)]
rank.sort()
arr = [i for i in range(1, N+1)]
answer = 0

for a, b in zip(rank, arr):
    answer += abs(a - b)
    
print(answer)