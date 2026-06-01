class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        for i in range(len(nums)):
            if nums[i] in compliments.keys():
                return [compliments[nums[i]], i]
            else: compliments[target-nums[i]] = i

        return None