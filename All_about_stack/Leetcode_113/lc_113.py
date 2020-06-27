

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
这题是真不会。
'''
class myNode(object):
    def __init__(self, p, is_leaf, count):
        self.parent = p
        self.is_leaf = is_leaf
        self.count = count
from collections import deque
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        return 0





