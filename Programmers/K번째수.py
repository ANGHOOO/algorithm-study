def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        temp = sorted(array[i-1:j])
        answer.append(temp[k-1])
        
    return answer