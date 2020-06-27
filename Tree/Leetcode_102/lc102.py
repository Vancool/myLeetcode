from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = deque()
        deque.append(root)
        preLevelNum = 1
        curLevelNum = 0
        res = []
        curRes = []
        while deque:
            cur = deque.popleft()
            curRes.append(cur.val)
            if cur.left:
                deque.append(cur.left)
                curLevelNum += 1
            if cur.right:
                deque.append(cur.right)
                curLevelNum += 1
            preLevelNum -= 1
            if preLevelNum == 0:
                res.append(curRes)
                preLevelNum = curLevelNum
                curLevelNum = 0
        return res

