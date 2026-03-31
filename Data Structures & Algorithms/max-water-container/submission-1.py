class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left=0
        right=len(heights)-1
        area=0

        while left<right:

            left_bound=heights[left]
            right_bound=heights[right]

            width=right-left

            area=max(area,min(left_bound,right_bound)*width)

            if left_bound<right_bound:
                left=left+1
            else:
                right=right-1
        
        return area


        