from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        a=deque()
        result=[]

        for i in range(len(nums)):
            while a and nums[i]>=nums[a[-1]]:
                a.pop()
            
            if a and a[0] < i-k+1: #i-k+1 is the left edge of the window ,the start of the widow so if the index is
                                    #since we are maintaiing a decrecing que and if the first elemtn index is < the start fo the edge it is not in the window and there cant be a maximum at that window.so we removew it 
                a.popleft()
            
            a.append(i)

            if i-k+1>=0: #this condtion (i-k+1 will give negative value until we have covered the window size once the window size is covered it will become positive and we ave start updating.Once it has becoe positive it will stay postive because we are moving the window 1 by 1 so lets say we have [1,2,3,4,5,6],noe wif window size is 3 unitl it sees [1,2,3])
                result.append(nums[a[0]]) # it will be -ve value once it has seen it will become positive .once (i-k+1) becomes positive , we have to update for every increment of i ,because lets say we are at 3rd index we have our window size is 3 [0,1,2]
                (                         #So when i moves it means it is the right end of the window and the window sizw can only be 3. So we have to make sure any values in deque is within the window(i-k+1,i)
                )
        
            
        return result




        
        