class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        area=0

        while left<right:
            if heights[left] < heights[right]:
                height=min(heights[left],heights[right])
                breadth=right-left
                area=max(area,height*breadth)
                left=left+1
            else:
                height=min(heights[left],heights[right])
                breadth=right-left
                area=max(area,height*breadth)
                left=left+1
        return area
            

        