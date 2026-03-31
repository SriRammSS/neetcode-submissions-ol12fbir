class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d={}

        for i in strs:
            alphabet_onehot=[0]*26

            for j in i:

                alphabet_onehot[ord(j)-ord('a')]=alphabet_onehot[ord(j)-ord('a')]+1

            key=tuple(alphabet_onehot)

            if key not in d:
                d[key]=[]
            d[key].append(i)
        
        return list(d.values())