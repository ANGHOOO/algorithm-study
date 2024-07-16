def solution(citations):
    answer = 0
    for h in range(10001):
        over_h = 0
        under_h = 0
        for citation in citations:
            if citation >= h:
                over_h += 1
            else:
                under_h += 1
        
        if under_h < h <= over_h:
            answer = max(answer, h)
            
    return answer