from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Prepend the length of the string and a delimiter
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        final_list = []
        i = 0
        
        while i < len(s):
            # Find the delimiter starting from position i
            j = i
            while s[j] != '#':
                j += 1
            
            # The number before '#' tells us the length of the string
            length = int(s[i:j])
            
            # Extract the actual string using the length
            # It starts right after '#' (j + 1) and ends at (j + 1 + length)
            start_str = j + 1
            end_str = start_str + length
            final_list.append(s[start_str:end_str])
            
            # Move our pointer i to the start of the next encoded block
            i = end_str
            
        return final_list