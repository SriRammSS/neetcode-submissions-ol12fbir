class Solution:
    def isValid(self, s: str) -> bool:

        pairs={")":"(","]":"[","}":"{"}

        stack=list()

        for i in s:
            if stack and i not in pairs.values():
                if stack[-1]==pairs[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if not stack:
            return True
        else:
            return False
        