class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        stack = []

        if len(s) == 0:
            return True

        if len(s) % 2 != 0:
            return False

        for c in s:
            if c in pairs:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if len(stack) != 0:
            return False

        return True