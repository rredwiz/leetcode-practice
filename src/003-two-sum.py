from leetcode_template import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        this is the brute force solution, not optimal

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        '''
        h = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in h:
                return [h[diff], i]
            h[n] = i
        return []
        # this solution is O(n) with O(n) space 