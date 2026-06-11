class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup={}
        for i,j in enumerate(nums):
            diff=target-j
            if diff in lookup.keys():
                return [lookup[diff],i]
            lookup[j]=i

            
        