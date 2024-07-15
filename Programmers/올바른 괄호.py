def solution(s):
    
    result = [s[0]]
    
    for i in range(1, len(s)):
        if s[i] == '(':
            result.append(s[i])
        else:
            if result:
                result.pop()
                
    if len(result) == 0:
        return True
    else:
        return False