from itertools import permutations, combinations

def solution(k, dungeons):
    answer = -1
    
    permu = list(permutations(dungeons))
    
    for p in permu:
        temp_piro = k
        count = 0
        for dungeon in p:
            piro, cost = dungeon
            if temp_piro >= piro:
                temp_piro -= cost
                count += 1
        answer = max(answer, count)
        
    return answer