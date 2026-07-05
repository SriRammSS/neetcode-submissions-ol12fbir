class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for i in range(len(matrix)):
            # 1. Check if the target could even be in this row
            if target > matrix[i][-1]:
                continue
            
            # 2. Reset pointers FOR EACH ROW we actually want to search
            low = 0
            high = len(matrix[i]) - 1
            
            # 3. Binary search the current row
            while low <= high:
                mid = (low + high) // 2  # Fixed parentheses
                
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
                    
            # If we finish the binary search for this row and didn't find it,
            # it means the target doesn't exist in the matrix at all (since rows are sorted).
            return False
            
        return False