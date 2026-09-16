class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}

        if len(s_freq) != len(t_freq):
            return False

        for c in s:
            s_freq[c] = s_freq.get(c, 0) + 1

        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1

        if s_freq == t_freq:
            return True

        return False