class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        L = 0
        R = n-1
        ans = []

        while L < R:
            cur = numbers[L] + numbers[R]
            if cur == target:
                return [L+1, R+1]

            if cur > target:
                R -= 1
            else: L += 1
            
        return []
            