def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    
    new_lost = []
    temp_lost = lost[::]
    temp_reserve = reserve[::]
    
    for l in lost:
        if l in temp_reserve:
            temp_lost.remove(l)
            temp_reserve.remove(l)
            
    for l in temp_lost:
        if l - 1 in temp_reserve:
            temp_reserve.remove(l - 1)
            continue
        elif l + 1 in temp_reserve:
            temp_reserve.remove(l + 1)
            continue
        new_lost.append(l)
        
    return n - len(new_lost)