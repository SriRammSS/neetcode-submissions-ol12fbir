class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti={}

        for i,j in enumerate(nums):
            diff=target-j

            if diff in dicti:
                return [dicti[diff],i]
            dicti[j]=i
