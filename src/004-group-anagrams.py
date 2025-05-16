from leetcode_template import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # creating a dictionary and setting it to a default dict
        # the default dict makes default value an empty list for each key
        h = defaultdict(list)
        
        # looping through all strings in the given list
        for s in strs:
            # creating a list with 26 characters, for the key of the dict
            count = [0] * 26
            
            # looping through each character in the string
            # adding the number of characters into the count list comprising the word
            for c in s:
                # we use ord to ingeniously index the letters by ascii into the list
                count[ord(c) - ord("a")] += 1

            # defaultdicts empty lists get appended the string to each anagram
            h[tuple(count)].append(s)
        
        return list(h.values())