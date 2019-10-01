from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        res = list(c.values())
        res.sort()
        return len(set(res)) == len(res)
