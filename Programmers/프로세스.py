def solution(priorities, location):
    answer = 0
    temp = []
    for i, p in enumerate(priorities):
        temp.append((i, p))
    
    while temp:
        # print(temp)
        idx, prior = temp.pop(0)
        max_prior = 0
        for i, p in temp:
            if p > max_prior:
                max_prior = p
                
        if prior >= max_prior:
            answer += 1
            if idx == location:
                return answer
        else:
            temp.append((idx, prior))
    