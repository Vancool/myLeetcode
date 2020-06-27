# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        if root == p or root == q:
            return root
        if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
            return root
        if p.val < root.val:
            return self.lowestCommonAncestor(root.left, p,q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
'''
其实这题可以不用递归，直接迭代就好
递归的话空间复杂度为O(n)
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        while root:
            val = root.val
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        return None
