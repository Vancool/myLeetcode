# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        def equalTree(left, right):
            if left == None and right == None:
                return True
            elif left and right:
                return (left.val == right.val and equalTree(left.left, right.left) and equalTree(left.right, right.right))
            return False
        return equalTree(root.left, root.right)