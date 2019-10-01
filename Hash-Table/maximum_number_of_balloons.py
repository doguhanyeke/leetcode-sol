from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c1 = Counter(text)
        res = 0
        while True:
            c2 = Counter("balloon")
            if len(c2 - c1) == 0:
                res += 1
            else:
                break
            c1 -= c2
        return res
