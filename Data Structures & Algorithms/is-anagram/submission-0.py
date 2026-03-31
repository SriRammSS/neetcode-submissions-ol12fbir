class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d={}


        for i in s:
            if i not in d.keys():
                a=1
            else:
                a=d[i]+1
            d[i]=a
        
        for i in t:
            if i in d.keys():
                d[i]=d[i]-1
            else:
                return False
        
        return all(x==0 for x in d.values())

            

   

    