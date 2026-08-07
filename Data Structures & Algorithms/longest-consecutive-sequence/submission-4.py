class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        longest = 1
        cur = 1

        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i-1]:
                cur += 1

            elif nums[i] == nums[i - 1]:
                continue

            else:
                cur = 1

            longest = max(longest, cur)

        return longest