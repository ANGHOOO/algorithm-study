def solution(name):
    answer = 0
    min_move = float('inf')
    
    for i in range(len(name)):
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        min_move = min(min_move, i * 2 + len(name) - next, i + 2 * (len(name) - next))
        
    answer += min_move
    
    return answer