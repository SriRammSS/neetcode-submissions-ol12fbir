from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d=defaultdict(list)

        for i in strs:
            alpha=[0]*26

            for j in i:
                alpha[ord(j)-ord('a')]=alpha[ord(j)-ord('a')]+1
            
            key=tuple(alpha)

            d[key].append(i)
        
        return list(d.values())
                
                

        