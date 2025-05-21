from leetcode_template import *

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool: 
        return len(nums) != len(set(nums))

# reviewed this on 05/21/2025