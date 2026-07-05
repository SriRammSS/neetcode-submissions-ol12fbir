class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        low=0
        high=len(matrix[-1])-1
        for i in range(len(matrix)):

            if target>matrix[i][high]:
                break
            else:
                while low<=high:
                    mid=low+high//2
                    if matrix[i][mid]==target:
                        return True
                    elif target < high:
                        high=mid-1
                    else:
                        low=mid+1
        return False
        