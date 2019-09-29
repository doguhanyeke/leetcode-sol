class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for i in arr2:
            result.extend([i] * arr1.count(i))
        remainder = [item for item in arr1 if item not in result]
        remainder.sort()
        result.extend(remainder)
        return result
