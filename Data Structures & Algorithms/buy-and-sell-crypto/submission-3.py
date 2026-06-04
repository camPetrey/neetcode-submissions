class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProf = 0

        while right < len(prices):
            if prices[left] >= prices[right]:
                left = right
                right += 1
                continue

            curProf = prices[right] - prices[left]
            if curProf > maxProf:
                maxProf = curProf
            else:
                right += 1

        return maxProf

