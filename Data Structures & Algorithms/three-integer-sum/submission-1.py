class Solution:
    # I wrote twoSum
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = 0
        r = len(nums) - 1
        res = []
        while l < r:
            twosum = nums[l] + nums[r]
            if twosum < target:
                l += 1
            elif twosum > target:
                r -= 1
            else:
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1

                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []

        nums = sorted(nums)
        curr = 0

        while curr < len(nums) - 2:
            
            target = 0 - nums[curr]

            if curr > 0 and nums[curr] == nums[curr - 1]:
                curr += 1
                continue

            pairs = self.twoSum(nums[curr + 1:], target)

            for pair in pairs:
                triple = [nums[curr]] + pair
                res.append(triple)

            curr += 1
            
        return res