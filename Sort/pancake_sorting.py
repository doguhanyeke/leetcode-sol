import heapq
from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        Alist = A[:]
        heapq._heapify_max(Alist)
        k = len(A)
        result = []
        while k > 1:
            target = heapq._heappop_max(Alist)
            ind = A.index(target)
            if ind != 0:
                self.swap_first_k_elements(A, ind + 1)
                result.append(ind + 1)
            self.swap_first_k_elements(A, k)
            result.append(k)
            k -= 1
        return result

    @staticmethod
    def swap_first_k_elements(given_list, k):
        temp_list = given_list[:k]
        given_list[:k] = temp_list[::-1]


if __name__ == '__main__':
    s = Solution()
    lst = [3, 2, 4, 1]
    print(s.pancakeSort(lst))
