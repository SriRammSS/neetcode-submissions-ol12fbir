class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        new_list=set(nums)
        largest_conseq=0

        for i in range(len(nums)):
            j=1
            check_number=nums[i]
            while check_number in new_list:
                if check_number+1 in new_list:
                    j=j+1
                check_number=check_number+1
            largest_conseq=max(largest_conseq,j)
        return largest_conseq


        