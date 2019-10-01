from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        c = Counter(S)
        ele = heapq.nlargest(1, c, key = lambda x: c[x])[0]
        value = c[ele]
        if len(S) < (value * 2 - 1):
            return ""
        else:
            remainder = [i for i in S if i != ele]
            i = 0
            res = ele
            value -= 1
            while value or i < len(remainder):
                res += remainder[i]
                i += 1
                if value > 0:
                    res += ele
                    value -= 1
            return res

if __name__ == '__main__':
    s = Solution()
    ans = s.reorganizeString("aab")
    print(ans)

