class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        most = 0

        while left < right:
            cur = min(heights[left], heights[right]) * (right - left)
            if cur > most:
                most = cur
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1

        return most
            

