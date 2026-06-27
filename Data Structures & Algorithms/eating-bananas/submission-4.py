import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (right + left) // 2

            tot_hours = 0
            for pile in piles:
                tot_hours += math.ceil(pile / mid)

            if tot_hours <= h:
                right = mid
            else: 
                left = mid + 1

        return left
            
            