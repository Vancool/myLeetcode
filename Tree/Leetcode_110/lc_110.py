# Definition for a binary tree node.
from Tree.TreeTool.lc_297 import Codec
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        def getHeightTree(root):
            if root == None:
                return None
            hNode = TreeNode(1)
            if root.left:
                hNode.left = getHeightTree(root.left)
                hNode.val += hNode.left.val
            if root.right:
                hNode.right = getHeightTree(root.right)
                hNode.val = max(hNode.val, 1 + hNode.right.val)
            return hNode
        def checkTree(root):
            if root == None:
                return True
            if root.right and root.left:
                if -1 <= root.right.val - root.left.val <= 1:
                    return checkTree(root.right) and checkTree(root.left)
                else:
                    return False
            if root.right:
                return root.right.val <= 1
            if root.left:
                return root.left.val <= 1
            return True

        heightTree = getHeightTree(root)
        res = checkTree(heightTree)
        return res


a = Solution()
treeTool = Codec()
tree = treeTool.deserialize('[1,2,2,3,3,null,null,4,4]')
print(a.isBalanced(tree))
print("Done")
