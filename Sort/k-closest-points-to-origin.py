import math
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda x: math.pow(x[0], 2) + math.pow(x[1], 2))[:K]


class Solution2:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heapq.heapify(points)
        return heapq.nsmallest(K, points, key=lambda x: x[0] * x[0] + x[1] * x[1])
