# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        if root == None: return []
        queue = deque()
        res = []
        queue.append(root.val)
        while queue:
            subres = []
            for i in range(len(queue)):
                root = queue.popleft()
                subres.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            if subres:
                res.append(subres)
        return res
