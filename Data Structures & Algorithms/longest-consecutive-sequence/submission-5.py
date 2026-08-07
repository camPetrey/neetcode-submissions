class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        long = 0
        cur = 0

        for num in nums:
            if num - 1 in nums:
                continue

            cur += 1
            while num + 1 in nums:
                cur += 1
                num += 1

            long = max(long, cur)
            cur = 0

        return long

            

            