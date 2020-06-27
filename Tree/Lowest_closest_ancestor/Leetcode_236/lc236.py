# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
这题我自己写得超乱
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == q:
            return p
        if root == None:
            return None
        parent = []
        self.find_q = False
        self.find_p = False
        def Process(root):
            if root == None:
                return
            Process(root.left)
            if self.find_q and self.find_p:
                parent.append(root)
                return
            curentP = self.find_p
            curentQ = self.find_q
            self.find_p = False
            self.find_q = False
            Process(root.right)
            self.find_p = curentP | self.find_p
            self.find_q = curentQ | self.find_q
            if self.find_q and self.find_p:
                parent.append(root)
                return
            if root == q:
                if self.find_p:
                    parent.append(q)
                self.find_q = True
            if root == p:
                if self.find_q:
                    parent.append(p)
                self.find_p = True


        Process(root)
        return parent[0]


