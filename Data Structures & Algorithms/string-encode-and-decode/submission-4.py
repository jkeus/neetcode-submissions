class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word))
            res += '#'
            res += word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l < len(s):
            lim = ""
            while s[l] != '#':
                lim += s[l]
                l += 1
            lim = int(lim)
            word = s[l+1:lim+l + 1]
            print(word, l, lim)
            res.append(word)
            l += lim + 1
        return res