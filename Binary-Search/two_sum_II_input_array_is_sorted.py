from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_searh(first, last):
            mid = int((first + last) / 2)
            print(first, mid, last)
            print(target, numbers[mid])
            if numbers[mid] == target:
                return mid
            elif numbers[mid] > target:
                binary_searh(first, mid - 1)
            else:
                binary_searh(mid + 1, last)
            return -1

        ind = binary_searh(0, len(numbers)-1)
        print(ind)

if __name__ == '__main__':
    s = Solution()
    input_list = [1, 3, 4, 7, 9, 11]
    s.twoSum(input_list, 1)
