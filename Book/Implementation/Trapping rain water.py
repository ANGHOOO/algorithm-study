from types import List 

class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        for w in range(1, len(height) - 1):
            left_max = max(height[:w])
            right_max = max(height[w+1:])
            compare = min(left_max, right_max)
            if height[w] < compare:
                answer += compare - height[w]

        return answer