from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Step 1: Count frequency of each number
        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] = d[nums[i]] + 1

        # Step 2: Group numbers by frequency
        c = defaultdict(list)
        for key, value in d.items():
            c[value].append(key)

        # Step 3: Bucket sort - index represents frequency (+1 to avoid out of range)
        e = [0] * (len(nums) + 1)
        for key, value in c.items():
            e[key] = value

        # Step 4: Iterate from highest frequency and collect k elements
        final = []
        for i in range(len(e) - 1, 0, -1):
            if e[i] == 0:
                continue
            else:
                final.extend(e[i])
            if len(final) >= k:
                break

        return final