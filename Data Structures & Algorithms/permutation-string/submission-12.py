from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        window_size=len(s1)
        

        s1_counter=Counter(s1)
        s2_counter={}

    

        j=0

        for i in range(len(s2)):

            if s2[i] not in s2_counter.keys():
                s2_counter[s2[i]]=1
            else:
                s2_counter[s2[i]]=s2_counter[s2[i]]+1
            
            
            if i-j+1==window_size:

                if s1_counter==s2_counter:
                    return True
                else:

                    s2_counter[s2[j]]=s2_counter[s2[j]]-1
                    
                    if s2_counter[s2[j]]==0:
                        s2_counter.pop(s2[j])
                    j=j+1
        return False
                    




            



    
        

        

        