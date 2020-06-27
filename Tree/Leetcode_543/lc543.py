# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        if root == None: return 0
        self.res = 0
        def getDepth(root):
            if root == None: return 0
            left = getDepth(root.left)
            right = getDepth(root.right)
            self.res = max(left + right, self.res)
            return max(left, right) + 1

        getDepth(root)
        return self.res

from Tree.TreeTool.lc_297 import Codec
c = Codec()
tree = c.deserialize('[1,2,3,4,5]')
a = Solution()
print(a.diameterOfBinaryTree(tree))
print("Done")