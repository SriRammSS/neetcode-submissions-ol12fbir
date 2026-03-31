class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        track=set(nums)
        count=0
        max_length=0

        for i in range(len(nums)):
            if nums[i]-1 not in track:
                count=0
                j=nums[i]
                while j in track:
                    count=count+1
                    j=j+1
                max_length=max(max_length,count)
        
        return max_length
            

        