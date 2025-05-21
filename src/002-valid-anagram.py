from leetcode_template import *

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t) op solution kinda cheating
        # return sorted(s) == sorted(t) fast solution but mid time complexity

        if len(s) != len(t):
            return False
        
        s_map, t_map = {}, {}
        
        for i in range(len(s)):
            s_map[s[i]] = 1 + s_map.get(i, 0) 
            t_map[t[i]] = 1 + s_map.get(i, 0)

        for c in s_map:
            if s_map[c] != t_map.get(c, 0):
                return False
        
        return True

        # in an updated solution we can also use defaultdicts since
        # these defaultdict(int) storages make it so we don't
        # need to worry about the default value 0 and improve logic

        # similarly using the .count string method with a set makes this
        # extremely fast:

        # if len(s) != len(t):
        #     return False

        # for c in set(s):
        #     if s.count(c) != t.count(c):
        #         return False
        
        # return True
            