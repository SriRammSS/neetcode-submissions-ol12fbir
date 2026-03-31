class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left=0

        right=len(heights)-1
        area=0

        while left<right:

            leftbound=heights[left]

            rightbound=heights[right]

            width=right-left

            area=max(area,min(leftbound,rightbound)*width)

            if heights[left]<heights[right]:
                left=left+1
            else:
                right=right-1
        
        return area



     

        