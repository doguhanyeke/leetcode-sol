# Definition for a binary tree node.
# class TreeNode(object):
#     def init(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.ans = 0

        def sum_all(node):
            if node is None: return
            sum_all(node.left)
            sum_all(node.right)
            if L <= node.val <= R:
                self.ans += node.val
            return
        sum_all(root)
        return self.ans
