from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        has=defaultdict(list)

        for i in range(len(strs)):
            alpha=[0]*26

            for j in strs[i]:
                alpha[ord(j)-ord("a")]=alpha[ord(j)-ord("a")]+1
            
            key=tuple(alpha)

            has[key].append(strs[i])
        
        return list(has.values())

        