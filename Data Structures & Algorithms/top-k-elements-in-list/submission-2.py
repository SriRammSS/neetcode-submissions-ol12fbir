from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] = d[nums[i]] + 1
        c = defaultdict(list)

        for key, value in d.items():
            c[value].append(key)
        e = [0] * (len(nums) + 1)

        for key, value in c.items():
            e[key] = value
        final = []
        
        for i in range(len(e) - 1, 0, -1):
            if e[i] == 0:
                continue
            else:
                final.extend(e[i])
            if len(final) >= k:
                break

        return final