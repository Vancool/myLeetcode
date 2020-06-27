class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from Tree.treeTool import createBinaryTree
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = []
        path = []
        def getPath(root, curVal):
            if root == None:
                return
            curVal -= root.val
            if curVal == 0 and not root.left and not root.right:
                res.append(path+[root.val])
                return
            path.append(root.val)
            if root.left:
                getPath(root.left, curVal)
            if root.right:
                getPath(root.right, curVal)
            path.pop()
        getPath(root, sum)
        return res
a = Solution()
t = createBinaryTree([5,4,8,11,'#', 13,4,7,2,'#','#',5,1])
print(a.pathSum(t,22))
print("Done")

