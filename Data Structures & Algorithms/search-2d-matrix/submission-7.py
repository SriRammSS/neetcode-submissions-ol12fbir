class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows=len(matrix)
        col=len(matrix[-1])

        low=0
        high=(rows*col)-1

        while low<=high:

            mid=(low+high)//2

            mid_ele=matrix[mid // col][mid % col]
            if mid_ele==target:
                return True
            elif mid_ele > target:
                high=mid-1
            else:
                low=mid+1
        
        return False

