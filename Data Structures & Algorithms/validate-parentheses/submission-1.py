class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(", "]":"[", "}":"{"}
        stack = list()
        
        for i in s:
            if i not in pairs.values():  # closing bracket
                if not stack or stack[-1] != pairs[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)  # opening bracket
        
        return not stack