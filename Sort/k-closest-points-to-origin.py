import math


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda x: math.pow(x[0], 2) + math.pow(x[1], 2))[:K]

