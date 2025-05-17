from leetcode_template import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = defaultdict(list)
        l = []

        for num in nums:
            h[num].append(num)
        
        for i in range(k):
            max_ = -1
            top_to_append = None
            for key, val in h.items():
                if len(val) > max_:
                    max_ = len(val)
                    top_to_append = key
            l.append(top_to_append)
            del h[top_to_append]
        
        return l

        # this solution is slow but it was what i came up with
        # will explore bucket sort and heaps at some point
