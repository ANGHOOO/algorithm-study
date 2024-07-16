def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5] * 10000
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * 10000
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 10000
    
    c1, c2, c3 = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == p1[i]:
            c1 += 1
        
        if answers[i] == p2[i]:
            c2 += 1
            
        if answers[i] == p3[i]:
            c3 += 1
    
    max_cnt = max(c1, c2, c3)
    temp = [c1, c2, c3]
    for i in range(len(temp)):
        if temp[i] == max_cnt:
            answer.append(i + 1)
            
    return answer