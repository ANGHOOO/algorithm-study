from itertools import product

def solution(word):
    answer = 0
    alphabet = ['A', 'E', 'I', 'O', 'U']
    arr = set()
    
    for i in range(1, 6):
        temp = list(product(alphabet, repeat=i))
        for alpha in temp:
            string = ''.join(alpha)
            arr.add(string)
            
    arr = sorted(list(arr))
    
    return arr.index(word) + 1