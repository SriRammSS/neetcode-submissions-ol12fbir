class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            breadth = right - left
            
            if heights[left] < heights[right]:
                current_area = heights[left] * breadth
                left += 1
            else:
                current_area = heights[right] * breadth
                right -= 1
                
            max_area = max(max_area, current_area)
        return max_area