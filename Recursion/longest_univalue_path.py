# Definition for a binary tree node.
# class TreeNode(object):
#     def init(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    sol = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def find_result(root):
            if root is None:
                return 0

            left_max = 0
            left_max += find_result(root.left)
            print left_max
            right_max = 0
            right_max += find_result(root.right)
            print right_max
            self.sol = max(self.sol, left_max, right_max)

            all_same = False
            if root.left and root.left.val == root.val and root.right and root.right.val == root.val:
                all_same = True
                self.sol = max(self.sol, 2 + left_max + right_max)
                return 1 + max(left_max, right_max)

            if not all_same and root.left and root.left.val == root.val:
                self.sol = max(self.sol, left_max + 1)
                return left_max + 1

            if not all_same and root.right and root.right.val == root.val:
                self.sol = max(self.sol, right_max + 1)
                return right_max + 1
            return 0

        find_result(root)
        return self.sol
