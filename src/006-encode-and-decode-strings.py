from leetcode_template import *

class Solution:
    def encode(self, strs: List[str]) -> str:

        # here we encode the string using integers and a delimiter
        # this produces the result 4*this4*that3*and4*this
        res = ""
        for s in strs:
            res += str(len(s)) + "*" + s
        return res
    
    def decode(self, s: str) -> List[str]:
        
        # we decode the string by following a two-pointer algorithm
        # we find the length of the string, and then we append that number
        # of characters after the delimiter
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "*":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        
        return res

        # tough trick for this problem honestly