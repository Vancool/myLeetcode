from Tree import treeTool
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
            return '[null]'
        queue = deque()
        queue.append(root)
        res = [str(root.val)]
        while len(queue) > 0:
            curNode = queue.popleft()
            if curNode.left:
                res.append(str(curNode.left.val))
                queue.append(curNode.left)
            else:
                res.append('null')
            if curNode.right:
                res.append(str(curNode.right.val))
                queue.append(curNode.right)
            else:
                res.append('null')
        while res[-1] == 'null':
            res.pop()
        return "["+','.join(res)+']'


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data= data[1:len(data)-1].split(',')
        if data[0] == 'null':
            return None

        # def getTree( s, index):
        #     if index >= len(s) or s[index] == 'null':
        #         return None
        #     root = TreeNode(int(s[index]))
        #     left = index * 2 + 1
        #     right = index * 2 + 2
        #     root.left = getTree(s, left)
        #     root.right = getTree(s, right)
        #     return root
        root = TreeNode(int(data[0]))
        count = 1
        queue = deque()
        queue.append(root)
        while count < len(data):
            curNode = queue.popleft()
            if data[count] != 'null':
                curNode.left = TreeNode(int(data[count]))
                queue.append(curNode.left)
            count += 1
            if count == len(data):
                break
            if data[count] != 'null':
                curNode.right = TreeNode(int(data[count]))
                queue.append(curNode.right)
            count += 1

        return root


if __name__ == "__main__":
    a = Codec()
    myT = a.deserialize("[4,2,5,1,3]")
    print(a.serialize(myT))
    print("Done!")


