from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = defaultdict(int)
        res = 0

        for num in nums:
            if num in seq:
                continue
            
            right = seq.get(num + 1, 0)
            left = seq.get(num - 1, 0)
            total = left + right + 1
            seq[num] = total
            seq[num - left] = total
            seq[num + right] = total

            if total > res:
                res = total
        
        return res