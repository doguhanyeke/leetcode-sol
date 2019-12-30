class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        result = 0
        while len(arr) > 1:
            mult = 225
            ind1 = ind2 = -1
            for i in range(len(arr[:-1])):
                tmp = arr[i] * arr[i + 1]
                if tmp < mult:
                    mult = tmp
                    ind1 = i
                    ind2 = i + 1
            result += arr[ind1] * arr[ind2]
            if arr[ind1] < arr[ind2]:
                arr.pop(ind1)
            else:
                arr.pop(ind2)
        return result
