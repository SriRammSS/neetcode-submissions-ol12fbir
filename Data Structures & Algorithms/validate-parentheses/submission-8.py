class Solution:
    def isValid(self, s: str) -> bool:
        valid_pair_set={"}":"{","]":"[",")":"("}
        stack=[]

        if s[0] in valid_pair_set.keys():
            return False
        

        for i in range(len(s)):
    

            if s[i] in valid_pair_set.values():
                stack.append(s[i])
            else:
                if stack and stack[-1] != valid_pair_set[s[i]]:
                    return False
                if stack and stack[-1] == valid_pair_set[s[i]]:
                    stack.pop()
        
        if len(stack)==0:
            return True
        else:
            return False
                
        
                
            
