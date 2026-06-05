class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        long = 0

        while left < right:
            curLeft = heights[left]
            curRight = heights[right]
            curHeight = min(curLeft, curRight) * (right - left)
            long = max(curHeight, long)

            if curLeft < curRight:
                left += 1
            else:
                right -= 1

        return long


