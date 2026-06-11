class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup=[]
        lookup.append(nums[0])

        for i in range(1,len(nums)):
            diff=abs(target-nums[i])
            if diff in lookup:
                return [lookup.index(diff),i]

            
        