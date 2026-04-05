class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        lookup=set()

        for i in range(len(nums)):
            if nums[i] not in lookup:
                lookup.add(nums[i])
            else:
                return nums[i]
        

        