import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2:
        first = heapq.heappop(scoville)
        
        if first < K:
            second = heapq.heappop(scoville)
            new = first + second * 2
            heapq.heappush(scoville, new)
            answer += 1
        else:
            break
        
    return -1 if scoville[0] < K else answer