# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
递归解法
'''
class Solution(object):
    def isSymmetric(self, root):
        def isMirror(left, right):
            if left is None and right is None: return True
            if left and right and left.val == right.val:
                return isMirror(left.left, right.right) and isMirror(left.right, right.left)
            return False
        if root == None: return True
        return isMirror(root.left, root.right)

'''
队列解法
'''
from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        if root == None: return True
        stack = deque()
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            left = stack.popleft()
            right = stack.popleft()
            if left is None and right is None:
                continue
            if left and right:
                if left.val == right.val:
                    stack.append(left.left)
                    stack.append(right.right)
                    stack.append(left.right)
                    stack.append(right.left)
                else:
                    return False
            else:
                return False
        return True

'''
栈解法
'''
class Solution(object):
    def isSymmetric(self, root):
        stackleft = []
        stackright = []
        curleft = root
        curright = root
        while curleft or curright or stackleft or stackright:
            if curleft and curright and curleft.val == curright.val:
                stackleft.append(curleft)
                stackright.append(curright)
                curleft = curleft.left
                curright = curright.right
            else:
                if curleft or curright: return False
                curleft = stackleft.pop()
                curright = stackright.pop()
                curleft = curleft.right
                curright = curright.left
        return True