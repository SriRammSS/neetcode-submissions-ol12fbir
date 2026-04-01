class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
# We will try to see which half of the side is sorted and see if the element exisit in that range or not. If it doesnt exisit in that part or half we explore the other half.
        while low<=high: #Here we use low<=high because the lement might or might not exisit
            mid=low+((high-low)//2)

            if nums[mid]==target:
                return mid

            if nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<=target<=nums[high]: #This means the left half is not sorted.
                    low=mid+1
                else:
                    high=mid-1
        return low if low<=high else -1

                    
                


