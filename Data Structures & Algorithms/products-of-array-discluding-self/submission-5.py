class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul=[1]*len(nums)
        suffix_mul=[1]*len(nums)
        final=[]

        for i in range(1,len(nums)):
            prefix_mul[i]=nums[i-1]*prefix_mul[i-1]
        for i in range(len(nums)-2,-1,-1):
            suffix_mul[i]=nums[i+1]*suffix_mul[i+1]
        for i,j in zip(prefix_mul,suffix_mul):
            final.append(i*j)
        
        return final

        


         

        