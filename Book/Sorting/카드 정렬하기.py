import heapq 
n = int(input())
heap = []
for _ in range(n):
    num = int(input())
    heapq.heappush(heap, num)

result = 0
while len(heap) != 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    sum_value = first + second 
    result += sum_value 
    heapq.heappush(heap, sum_value)

print(result)