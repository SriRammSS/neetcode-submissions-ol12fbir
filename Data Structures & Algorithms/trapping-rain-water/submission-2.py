class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1   # ❌ you had right=0, should start at end
        water_held = 0
        max_left = height[left]
        max_right = height[right]

        while left < right:
            if max_left < max_right:
                left = left + 1
                max_left = max(max_left, height[left])
                water_held += max_left - height[left]
            else:
                right = right - 1
                max_right = max(max_right, height[right])
                water_held += max_right - height[right]

        return water_held
