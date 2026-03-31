from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        a=deque()
        result=[]

        for i in range(len(nums)):
            while a and nums[i]>=nums[a[-1]]:
                a.pop()
            
            if a and a[0] < i-k+1:
                a.popleft()
            
            a.append(i)

            if i-k+1>=0:
                result.append(nums[a[0]])
        
            
        return result




        
        