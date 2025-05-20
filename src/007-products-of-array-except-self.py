from leetcode_template import *

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        this is O(n^2) so it's not the best solution       
        can we come up with a better solution?

        res = []

        for i in range(len(nums)):
            num = 1
            for j in range(len(nums)):
                if i != j:
                    num *= nums[j]
            res.append(num)        

        return res
        '''
        return [] # for no errors