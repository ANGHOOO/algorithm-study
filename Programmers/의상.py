def solution(clothes):
    answer = 1
    closet = dict()
    for v, k in clothes:
        if k in closet:
            closet[k].append(v)
        else:
            closet[k] = [v]
            
    for k, v in closet.items():
        answer *= (len(v) + 1)
        
    return answer - 1