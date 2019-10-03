# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []

        def inorder_traverse(root: TreeNode):
            if root is None:
                return
            inorder_traverse(root.left)
            res.append(root.val)
            inorder_traverse(root.right)

        inorder_traverse(root)
        # print(res)
        return res[k - 1]
