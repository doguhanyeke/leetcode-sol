# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        d = dict()
        def filld(r, h):
            if r is None:
                return
            if r.left is None and r.right is None:
                if h in d:
                    d[h] += r.val
                else:
                    d[h] = r.val
                return
            filld(r.left, h+1)
            filld(r.right, h+1)
            return
        filld(root, 0)
        l = d.keys()
        return d[max(l)]
