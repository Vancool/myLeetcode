# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if root == None: return True
        def Process(left, right):
            if left == None: return right == None
            if right == None: return left == None
            return left.val == right.val and Process(left.left, right.right) and Process(left.right, right.left)
        return Process(root.left, root.right)

from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        if root == None: return True

        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            left = queue.popleft()
            right = queue.popleft()
            if left == None and right == None:
                continue
            if left == None or right == None or left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True