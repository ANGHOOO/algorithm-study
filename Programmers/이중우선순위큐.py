import heapq 

def solution(operations):
    answer = []
    max_heap = []
    min_heap = []
    
    for operation in operations:
        oper, num = operation.split()
        num = int(num)
        
        if oper == 'I': # 삽입 연산
            heapq.heappush(max_heap, (-1 * num, num))
            heapq.heappush(min_heap, (num, -1 * num))
        else: # 삭제 연산
            if len(max_heap) == 0:
                continue
            if num == 1: # 큐에서 최댓값 삭제
                max_num = heapq.heappop(max_heap)[0]
                min_heap.remove((-1 * max_num, max_num))
            else: # 큐에서 최솟값 삭제
                min_num = heapq.heappop(min_heap)[0]
                max_heap.remove((-1 * min_num, min_num))
    
    if len(max_heap) == 0:
        return [0, 0]
    else:
        max_num = heapq.heappop(max_heap)[1]
        min_num = heapq.heappop(min_heap)[0]
        return [max_num, min_num]