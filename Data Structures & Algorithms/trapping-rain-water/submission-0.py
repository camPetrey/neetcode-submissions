class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        tallLeft = height[left]
        tallRight = height[right]
        total = 0;

        while left < right:

            if tallLeft < tallRight:
                left += 1
                tallLeft =  max(height[left], tallLeft)
                total += tallLeft - height[left]

            else:
                right -= 1
                tallRight =  max(height[right], tallRight)
                total += tallRight - height[right]

        return total


            



