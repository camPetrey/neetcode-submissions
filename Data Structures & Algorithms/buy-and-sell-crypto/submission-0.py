class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = 0
        right = 0
        maxPro = 0

        while right != n:
            if prices[right] < prices[left]:
                left = right
            curPro = prices[right] - prices[left]
            if curPro > maxPro:
                maxPro = curPro

            right += 1

        return maxPro


