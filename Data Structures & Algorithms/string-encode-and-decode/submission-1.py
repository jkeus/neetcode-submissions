class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            op = str(len(word))
            res = res + op + '#' + word

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            key = ""
            
            while s[i] != '#':
                key += s[i]
                i += 1   
                
            length = int(key)
            word = s[i + 1 : i + 1 + length]
            res.append(word)
            
            i = i + 1 + length
        return res