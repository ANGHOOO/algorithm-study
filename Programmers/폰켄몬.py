def solution(nums):
    answer = 0
    length = len(nums) // 2
    set_nums = set(nums)
    
    return len(list(set_nums)[:length])