class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        res = True

        while l < r:
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
                continue
            
            if l != r:
                if not (s[l].isalpha() or s[l].isnumeric()):
                    l += 1
                    continue
                if not (s[r].isalpha() or s[r].isnumeric()):
                    r -= 1
                    continue
                res = False
                print(l, s[l], r, s[r])
                break
        return res