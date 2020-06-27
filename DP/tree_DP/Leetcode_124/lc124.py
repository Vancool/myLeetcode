# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        self.res = root.val

        def dp_process(root):
            if root == None:
                return 0
            left = dp_process(root.left)
            right = dp_process(root.right)
            one_leaf = max(left, right,0) + root.val
            two_leaf = left + right + root.val
            #one_leaf = one_leaf + root.val if one_leaf >= 0 else root.val
            self.res = max(self.res, one_leaf, two_leaf)
            return one_leaf
        dp_process(root)
        return self.res
