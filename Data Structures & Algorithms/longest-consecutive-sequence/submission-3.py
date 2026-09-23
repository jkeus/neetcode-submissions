from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = defaultdict(int)
        res = 0

        for num in nums:
            if num in vals:
                continue
            prev = vals.get(num - 1, 0)
            post = vals.get(num + 1, 0)
            curr = prev + post + 1
            vals[num] = curr
            vals[num - prev] = curr
            vals[num + post] = curr
            if curr > res:
                res = curr   
        return res
