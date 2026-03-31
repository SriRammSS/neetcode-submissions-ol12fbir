class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unums=set(nums)
        cont=0

        for i in unums:
            j=i

            if i-1 not in unums:

                while j in unums:

                    j=j+1
            cont=max(cont,j-i)
        return cont



        

                
        