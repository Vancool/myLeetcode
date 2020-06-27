# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root == None or root == p or root == q:
            return root
        self.res = None
        def Process(root):
            if root == None:
                return False
            left = Process(root.left)
            right = Process(root.right)
            if left and right:
                self.res = root
            if root == p or root == q:
                if left or right:
                    self.res = root
                else:
                    return True
            return False
        Process(root)
        return self.res