class Solution:
    def trap(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1

        left_wall=heights[left]

        right_wall=heights[right]

        water=0

        while left<right:
            if left_wall < right_wall:
                left=left+1
                left_wall=max(left_wall,heights[left])
                water=water+(left_wall-heights[left])
            else:
                right=right-1
                right_wall=max(right_wall,heights[right])
                water=water+(right_wall-heights[right])
        return water

