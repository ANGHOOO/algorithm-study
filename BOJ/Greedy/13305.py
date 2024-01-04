import sys
input = sys.stdin.readline

N = int(input())
dists = list(map(int, input().split()))
prices = list(map(int, input().split()))

answer = dists[0] * prices[0]
min_price = prices[0]

for i in range(1, len(dists)):
    if min_price > prices[i]:
        min_price = prices[i]
    answer += dists[i] * min_price
    
print(answer)