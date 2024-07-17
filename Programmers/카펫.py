def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            w = i
            h = yellow // i
            width = w + 2
            height = h + 2
            if width * height == brown + yellow:
                answer.append((width, height))
                
    answer.sort(key = lambda x : -x[0])
    return answer[0]