class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #nlogn
        for i in range(len(nums)): # * n 

            if i > 0 and nums[i] == nums[i -1]:
                continue

            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right: 
                cur = nums[left] + nums[right]
                if cur > target:
                    right -= 1
                elif cur < target:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left +=1

        return res




         