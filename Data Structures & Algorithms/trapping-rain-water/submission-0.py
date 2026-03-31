class Solution:
    def trap(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxLeft = heights[left]
        maxRight = heights[right]
        water = 0

        while left < right:
            if maxLeft <= maxRight:
                left = left + 1
                maxLeft = max(maxLeft, heights[left])
                water += maxLeft - heights[left]
            else:
                right = right - 1
                maxRight = max(maxRight, heights[right])
                water += maxRight - heights[right]

        return water

