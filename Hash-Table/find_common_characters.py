from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = Counter(list(map(lambda x: str(x), A[0])))
        for i in A[1:]:
            char_list = Counter(list(map(lambda x: str(x), i)))
            res = res & char_list
        result = []
        for i in res:
            value = res[i]
            while value:
                result.append(i)
                value -= 1
        return result
