class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixproduct=[1] * len(nums)
        suffixproduct=[1] *len(nums)
        a=1

        for i in range(1,len(nums)):
            a=a*nums[i-1]
            prefixproduct[i]=a
        b=1
        for i in range(len(nums)-2,-1,-1):
            b=b*nums[i+1]
            suffixproduct[i]=b
        
        result=[]

        for i in range(len(prefixproduct)):
            result.append(suffixproduct[i]*prefixproduct[i])
        
        return result
        

        