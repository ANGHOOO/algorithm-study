def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    temp = sorted(numbers, key = lambda x : x*3, reverse=True)
    
    answer = answer.join(temp)
    
    return str(int(answer))