class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l = 0
        r = len(numbers) - 1

        while l < r:
            cursum = numbers[l] + numbers[r]
            if target < cursum:
                r -= 1
            elif target > cursum:
                l += 1
            else:
                res = [l + 1, r + 1]
                break

        return res