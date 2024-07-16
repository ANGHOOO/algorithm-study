from itertools import permutations

def is_sosu(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True

def solution(numbers):
    answer = 0
    arr = set()
    
    for i in range(1, len(numbers)+1):
        temp = list(permutations(numbers, i))
        for num in temp:
            n = ''.join(num)
            arr.add(int(n))
            
    for num in arr:
        if is_sosu(num):
            # print(num)
            answer += 1
            
    return answer