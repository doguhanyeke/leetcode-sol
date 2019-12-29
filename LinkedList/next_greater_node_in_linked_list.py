# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
from typing import List
import heapq


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        lst = []
        heap_lst = []
        return_lst = [0]
        current = head
        while current:
            lst.append(current.val)
            current = current.next
        heapq.heappush(heap_lst, lst.pop())
        while len(lst) != 0:
            val = lst.pop()

            while len(heap_lst) != 0 and heap_lst[0] <= val:
                heapq.heappop(heap_lst)
            if len(heap_lst) == 0:
                return_lst.append(0)
            else:
                return_lst.append(heap_lst[0])
            heapq.heappush(heap_lst, val)

        return return_lst[::-1]