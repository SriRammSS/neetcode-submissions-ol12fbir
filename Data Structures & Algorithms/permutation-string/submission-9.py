from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s2_counter=Counter(s2)

    

        for i in s1:
            if i in s2_counter.keys():
                s2_counter[i]=s2_counter[i]-1
            else: 
                return False
            if s2_counter[i]<0:
                return False
        
        return all(s2_counter.get(k)==0 for k in s1)
        



    
        

        

        