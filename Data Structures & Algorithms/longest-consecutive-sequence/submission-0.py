class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        final_nums=set(nums)

        best=0

        for i in final_nums:

            if i-1 not in final_nums:

                y=i

                while y in final_nums:
                    y=y+1
                
                best=max(best,y-i)
        return best
        