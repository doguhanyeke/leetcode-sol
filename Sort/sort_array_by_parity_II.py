class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        def next_even(i):
            while A[i] % 2 != 0:
                i += 1
            return i

        def next_odd(i):
            while A[i] % 2 == 0:
                i += 1
            return i

        def swap_elements(lst, i, j):
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

        for ind, ele in enumerate(A):
            if ind % 2 == 0:
                if ele % 2 == 0:
                    continue
                else:
                    index = next_even(ind + 1)
                    swap_elements(A, index, ind)
            else:
                if ele % 2 != 0:
                    continue
                else:
                    index = next_odd(ind + 1)
                    swap_elements(A, index, ind)
        return A

