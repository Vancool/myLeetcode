# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        res = []
        while root:
            res.append(root.val)
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root.right
                root.right = root.left
            root = root.right
        return res
'''
自己写的不可还原版的 Morris 算法
可以还原版的是下面的那个
'''
class Solution(object):
    def preorderTraversal(self, root):
        res = []
        while root:
            if root.left:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right
                if pre.right is None:
                    pre.right = root
                    res.append(root.val)
                    root = root.left
                elif pre.right == root:
                    pre.right = None
                    root = root.right
            else:
                res.append(root.val)
                root = root.right
        return res


'''
用栈的两种写法
还是第一种好理解一些
'''
class Solution(object):
    def preorderTraversal(self, root):
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            root = stack.pop()
            root = root.right
        return res
'''
第二种， 秘诀在于先append right 再 append left
'''
class Solution(object):
    def preorderTraversal(self, root):
        res = []
        if root == None:return res
        stack = []
        stack.append(root)
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res


