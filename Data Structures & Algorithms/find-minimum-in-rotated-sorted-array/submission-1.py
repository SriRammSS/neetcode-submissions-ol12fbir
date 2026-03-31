class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1

        while low< high:
            mid=low+((high-low)//2
            )

            if nums[mid] < nums[high]: #when nums[mid] < nums[high] from mid to high it is sorted .So the numbers is going to be in ascending order. Since we want the lowest elemnet we have to search back of it so high=mid. In this case the min can be either mid or back of it
                high=mid
            else:
                low=low+1 #if the other way nums[mid] > num[high] then there must be a dip or change in number magnitude like [3, 4, 5, 6, 1, 2] ,so we might have the min number in the right space.
        
        return nums[low
        ]
        