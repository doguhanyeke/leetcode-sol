# Definition for a binary tree node.
# class TreeNode(object):
#     def init(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys


class Solution(object):

    def minDiffInBST(self, root):
        self.ans = sys.maxint
        """
        :type root: TreeNode
        :rtype: int
        """
        def min_value(node):
            if node is None: return None, None, None
            if node and node.left is None and node.right is None: return node.val, node.val, node.val
            (leftminval, leftownval, leftmaxval) = min_value(node.left)
            (rightminval, rightownval, rightmaxval) = min_value(node.right)
            if leftmaxval:
                self.ans = min(self.ans, node.val - leftmaxval)
            else:
                leftminval = node.val
            if rightminval:
                self.ans = min(self.ans, rightminval - node.val)
            else:
                rightmaxval = node.val
            if leftownval:
                self.ans = min(self.ans, node.val - leftownval)
            if rightownval:
                self.ans = min(self.ans, rightownval - node.val)
            return leftminval, node.val, rightmaxval
        min_value(root)
        return self.ans
