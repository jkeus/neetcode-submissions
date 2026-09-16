class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        locs = {}
        res = []
        for i, num in enumerate(nums):
            diff = target - num
            if diff in locs:
                res = [locs[diff], i]
                break

            locs[num] = i
        return res


