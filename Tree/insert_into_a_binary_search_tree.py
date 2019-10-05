# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            root = TreeNode(val)
            return root
        tmp_root = root
        while tmp_root is not None:
            if tmp_root.val > val:
                if tmp_root.left is None:
                    tmp_root.left = TreeNode(val)
                    return root
                else:
                    tmp_root = tmp_root.left
            else:
                if tmp_root.right is None:
                    tmp_root.right = TreeNode(val)
                    return root
                else:
                    tmp_root = tmp_root.right


