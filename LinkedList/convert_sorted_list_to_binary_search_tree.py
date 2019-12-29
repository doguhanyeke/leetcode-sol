# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        size = 0
        current = head
        lst = []
        while current:
            lst.append(current.val)
            current = current.next
            size += 1

        def construct_tree(l, r):
            if l > r:
                return None
            mid = int((l + r) / 2)
            root = TreeNode(lst[mid])
            root.left = construct_tree(l, mid - 1)
            root.right = construct_tree(mid + 1, r)
            return root

        return construct_tree(0, size - 1)
