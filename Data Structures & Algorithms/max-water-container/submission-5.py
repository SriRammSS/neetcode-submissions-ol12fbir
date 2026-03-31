class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left=0
        right=len(heights)-1
        max_area=0


        while left < right:
            if heights[right] > heights[left]:
                width=right-left
                area=width*min(heights[left],heights[right])
                max_area=max(max_area,area)
                left=left+1
            else:
                width=right-left
                area=width*min(heights[left],heights[right])
                max_area=max(max_area,area)
                right=right-1
        return max_area

                
            
            
        