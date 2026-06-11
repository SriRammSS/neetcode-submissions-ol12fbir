from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution=defaultdict(list)

        for i in strs:
            num_count=[0]*26
            for j in i:
                num_count[ord(j)-97]=num_count[ord(j)-97]+1
            solution[tuple(num_count)].append(i)
        
        return list(solution.values())

        