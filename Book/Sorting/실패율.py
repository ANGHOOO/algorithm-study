def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1, N+1):
        count = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            fail = count / length
            
        answer.append((i, fail))
        length -= count 
        
    answer.sort(key = lambda x : (-x[1], x[0]))
    result = [answer[i][0] for i in range(len(answer))]
    return result