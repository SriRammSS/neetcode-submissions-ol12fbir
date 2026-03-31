class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i=0
        product=[]

        while i < len(nums):
            j=0
            multi=1

            while j < len(nums):

                if j!=i:
                    multi=multi*nums[j]
                j=j+1
            product.append(multi)

            i=i+1
        
        return product