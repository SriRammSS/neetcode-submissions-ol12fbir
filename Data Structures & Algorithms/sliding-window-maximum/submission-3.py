from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        a=deque()

        b=[]

        for i in range(len(nums)):

            while a and nums[i] >= nums[a[-1]]:
                a.pop()
            
            a.append(i)

            if a and a[0] < i-k+1:
                a.popleft()


            if i-k+1>=0:
                b.append(nums[a[0]])
        return b

        