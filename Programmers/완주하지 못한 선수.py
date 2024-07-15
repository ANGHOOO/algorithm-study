from collections import Counter

def solution(participant, completion):
    answer = []
    Pcounter = Counter(participant)
    Ccounter = Counter(completion)
    
    result = dict(Pcounter - Ccounter)
    
    for v in result:
        answer.append(v)
        
    return answer[0]
    