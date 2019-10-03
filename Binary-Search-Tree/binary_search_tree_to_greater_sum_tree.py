# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        d = {}

        def bst_recursive(root: TreeNode):
            if root is None:
                return

            bst_recursive(root.right)

            if all(root.val > x for x in d.keys()):
                d[root.val] = root.val
            else:
                # find just bigger than itself
                val = root.val
                while val not in d.keys():
                    val += 1
                d[root.val] = d[val] + root.val
                root.val = d[root.val]

            bst_recursive(root.left)
            return

        bst_recursive(root)
        # print(d)
        return root
