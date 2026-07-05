
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        min_time=float('infinity')

        while low <=high:

            mid=(low+high)//2

            total_hours = sum((pile + mid - 1) // mid for pile in piles)

            if total_hours > h:
                low=mid+1
            elif total_hours <=h:
                min_time=min(min_time,mid)
                high=mid-1
        
        return min_time
            

            

        
        