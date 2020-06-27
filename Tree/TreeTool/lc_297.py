class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return '[]'
        res = []
        queue = deque()
        queue.append(root)
        res.append(str(root.val))
        while queue:
            cur = queue.popleft()
            if cur.left:
                res.append(str(cur.left.val))
                queue.append(cur.left)
            else:
                res.append('null')
            if cur.right:
                res.append(str(cur.right.val))
                queue.append(cur.right)
            else:
                res.append('null')
        while res[-1] == 'null':
            res.pop()
        return '['+ ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data[1:len(data)-1]
        if len(data) == 0:
            return None
        data = data.split(',')
        root = TreeNode(int(data[0]))
        queue = deque()
        queue.append(root)
        i = 1
        while i < len(data):
            cur = queue.popleft()
            if data[i] != 'null':
                cur.left = TreeNode(int(data[i]))
                queue.append(cur.left)
            i += 1
            if i >= len(data):
                break
            if data[i] != 'null':
                cur.right = TreeNode(int(data[i]))
                queue.append(cur.right)
            i += 1
        return root
