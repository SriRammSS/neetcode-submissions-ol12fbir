class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stnums=set(nums)

        if len(stnums)==len(nums):
            return False
        else:
            return True
        