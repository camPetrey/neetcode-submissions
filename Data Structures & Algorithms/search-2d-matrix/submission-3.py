class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + (right - left) // 2) 
            cur = matrix[mid][0]
            if cur > target:
                right = mid - 1
            else: left = mid + 1

        row = right

        right = len(matrix[0]) - 1
        left = 0
        while left <= right:
            mid = left + (right - left) // 2
            cur = matrix[row][mid]
            if cur == target:
                return True
            if cur > target:
                right = mid - 1
            else: left = mid + 1
        return False