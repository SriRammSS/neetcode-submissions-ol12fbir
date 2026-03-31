from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        

        while low<=high:
            mid=low+((high-low)//2)

            score=sum([ceil(j/mid) for j in piles])

            if score<=h: #if the monkey eats at higher rate this condition will satisfy,so we are downplaiying the eating rate and see if there exisit some other minimum speed that can achieve eating all in h hours
                final=mid
                high=mid -1
            else: #this happens when the monkey eats slow so we shift low to mid and fast up the eating rate
                low = mid+1
        return final

        