class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        occur = {}

        for num, freq in freqs.items():
            occur.setdefault(freq, []).append(num)

        res = []
        
        for freq in sorted(occur, reverse=True):
            nums_with_freq = occur[freq]

            remaining = k - len(res)
            res.extend(nums_with_freq[:remaining])

            if len(res) == k:
                break

        return res

        