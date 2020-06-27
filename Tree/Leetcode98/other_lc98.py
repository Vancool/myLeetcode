# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
做有关 AVL的东西，最好先考虑中序遍历做
中序遍历 ： 1. 递归 2. 栈

自己是用后序遍历做的
后序遍历也可以写法很简单，自己还是写太复杂了
'''
class Solution(object):
    def isValidBST(self, root):
        self.pre = - float("inf")
        def Process(root):
            if root == None:
                return True
            if not Process(root.left):
                return False
            if self.pre >= root.val:
                return False
            self.pre = root.val
            if not Process(root.right):
                return False
            return True
        return Process(root)

'''
栈的中序遍历
'''
class Solution(object):
    def isValidBST(self, root):
        if root == None:
            return True
        stack = []
        cur = root
        pre = -float('inf')
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val <= pre:
                return False
            pre = cur.val
            cur = cur.right
        return True

'''
前序遍历写法，要写范围
真是简洁啊...
'''
class Solution(object):
    def isValidBST(self, root):

        def Process(root, minval, maxval):
            if root == None:
                return True
            if root.val >= maxval or root.val <= minval:
                return False
            return Process(root.left, minval, root.val) and Process(root.right, root.val, maxval)
        return Process(root, -float('inf'), float('inf'))