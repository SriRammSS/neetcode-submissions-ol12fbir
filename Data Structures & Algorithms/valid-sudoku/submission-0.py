from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        column=defaultdict(set)
        box=defaultdict(set)

        for row in range(9):
            for col in range(9):
                value=board[row][col]

                if value==".":
                    continue
                
                if (value in rows[row] or value in column[col] or value in box[row//3,col//3]):
                    return False
                
                rows[row].add(value)
                column[col].add(value)
                box[row//3,col//3].add(value)
        
        return True
   