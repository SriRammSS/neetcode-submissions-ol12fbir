from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d={}

        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        
        gd=defaultdict(list)

        for i,j in d.items():
            gd[j].append(i)

        sorte=[0]*(len(nums)+1)

        for i,j in gd.items():

            sorte[i]=gd[i]

        final=[]
  
    

        for i in range(len(sorte)-1,-1,-1):
            if sorte[i]==0:
                continue
            else:
                final.extend(sorte[i])
            if len(final)==k:
                break
        return final




        

    
        

            