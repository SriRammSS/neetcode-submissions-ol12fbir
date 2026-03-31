class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        d={}

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]=d[s[i]]+1

        for i in range(len(t)):

            if t[i] not in d:
                
                return False
            else:
                d[t[i]]=d[t[i]]-1
            
            if d[t[i]]<0:
                return False
        
        return all(x==0 for x in d.values())
            

        

        

            

   

    