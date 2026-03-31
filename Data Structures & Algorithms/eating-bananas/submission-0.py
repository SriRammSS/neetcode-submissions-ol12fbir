from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        

        while low<=high:
            mid=low+((high-low)//2)

            score=sum([ceil(j/mid) for j in piles])

            if score<=h:
                final=mid
                high=mid -1
            else:
                low = mid+1
        return final

        