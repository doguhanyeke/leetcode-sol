# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        tmp_root = root
        while tmp_root:
            if tmp_root.val == val:
                return tmp_root
            elif tmp_root.val > val:
                tmp_root = tmp_root.left
            else:
                tmp_root = tmp_root.right
        if tmp_root is None:
            return None
