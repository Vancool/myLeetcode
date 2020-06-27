# Definition for a binary tree node.
from Tree.TreeTool.lc_297 import Codec
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        res = []
        def recur(root, sum, path):
            if root == None :
                return
            if root.left == None and root.right == None:
                if sum - root.val == 0:
                    res.append(path + [root.val])
                return
            recur(root.left, sum - root.val, path + [root.val])
            recur(root.right, sum - root.val, path +[root.val])
        recur(root, sum, [])
        return res

a = Solution()
c = Codec()
tree = c.deserialize('[5,4,8,11,null,13,4,7,2,null,null,5,1]')
print(a.pathSum(tree, 22))