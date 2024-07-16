def solution(sizes):
    answer = 0
    max_list = []
    min_list = []
    for size in sizes:
        w, h = size
        max_list.append(max(w, h))
        min_list.append(min(w, h))
        
        
    return max(max_list) * max(min_list)