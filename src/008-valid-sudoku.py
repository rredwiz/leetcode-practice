from leetcode_template import *

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we need to loop through all rows and check for dupes
        for r in range(9):
            s = set()
            for c in range(9):
                spot = board[r][c]
                if spot == ".":
                    continue
                elif spot in s:
                    return False
                else:
                    s.add(spot)                        
        # we need to loop through all cols and check for dupes
        for r in range(9):
            s = set()
            for c in range(9):
                spot = board[c][r]
                if spot == ".":
                    continue
                elif spot in s:
                    return False
                else:
                    s.add(spot)
        # we need to loop through all boxes and check for dupes
        for box in range(9):
            s = set()
            for i in range(3):
                for j in range(3):
                    row = (box // 3) * 3 + i
                    col = (box % 3) * 3 + j
                    spot = board[row][col]
                    if spot == ".":
                        continue
                    elif spot in s:
                        return False
                    else:
                        s.add(spot)
        
        return True
        # this brute force solution is pretty good here
        # complex logic at row and col for the box checking, trick is to use integer div
        # the algorithm will ensure the correct row and column of each box we iterate through