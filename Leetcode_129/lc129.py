# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        if root == None: return 0
        def getValue(father_value, root):
            if root == None:
                return 0
            else:
                res = father_value * 10 + root.val
                left = getValue(res, root.left)
                right = getValue(res, root.right)
                return left + right if root.left or root.right else res
        return getValue(0, root)

class Solution(object):
    def sumNumbers(self, root):
        if root == None: return 0
        self.res = 0
        def getValue(father_value, root):
            if not root.left and not root.right:
                self.res += father_value * 10 + root.val
                return
            if root.left:
                getValue(father_value + root.val, root.left)
            if root.right:
                getValue(father_value + root.val, root.right)
        getValue(root)
        return self.res