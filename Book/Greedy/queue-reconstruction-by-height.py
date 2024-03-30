import heapq 
people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
heap = []
result = []

for p in people:
    heapq.heappush(heap, (-p[0], p[1]))

while heap:
    person = heapq.heappop(heap)
    result.insert(person[1], [-person[0], person[1]])

print(result)