
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque
class Solution(object):
    def connect(self, root):
        if root == None: return root
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                l = queue.popleft()
                if l.left: queue.append(l.left)
                if l.right: queue.append(l.right)
                if queue and i != size-1:
                    l.next = queue[0]
        return root

'''
这个解法不符合空间复杂度 O(1)的要求
看 others 

'''