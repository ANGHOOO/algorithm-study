from types import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answers = []
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    answers.append([i, j])
                    break

        return answers[0]
        