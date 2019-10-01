import heapq
from collections import Counter


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        c = Counter(A)
        return heapq.nlargest(1, list(c.keys()), key= lambda x: c[x])[0]
