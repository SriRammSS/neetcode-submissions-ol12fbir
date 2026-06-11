from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_count=Counter(s)

        for i in t:
            if i not in freq_count.keys() or freq_count[i]<0:
                return False
            else:
                freq_count[i]=freq_count[i]-1
        
        return all(value ==0 for value in freq_count.values())
        
        