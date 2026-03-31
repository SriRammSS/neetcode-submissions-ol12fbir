class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d={}

        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        

        for j in t:
            if j in d:
                d[j]=d[j]-1
            else:
                return False
        
            if d[j]<0:
                return False
        
        return all(x==0 for x in d.values())

        

            

   

    