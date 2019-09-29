class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        dict2 = {}
        for i in nums1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        for i in nums2:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1
        result = []
        size1 = len(dict1)
        size2 = len(dict2)
        if size1 < size2:
            for i in dict1.keys():
                if i in dict2:
                    result.extend(min(dict1[i], dict2[i]) * [i])
        else:
            for i in dict2.keys():
                if i in dict1:
                    result.extend(min(dict1[i], dict2[i]) * [i])
        return result
