from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d=defaultdict(list)

        for i in strs:
            alphabet_onehot=[0]*26

            for j in i:

                alphabet_onehot[ord(j)-ord('a')]=alphabet_onehot[ord(j)-ord('a')]+1

            key=tuple(alphabet_onehot)

            d[key].append(i)
        
        return list(d.values())