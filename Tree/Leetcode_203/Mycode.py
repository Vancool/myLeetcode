class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from Tree import treeTool
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if k == 0:
            return None
        # write code here
        path = []

        def getKval(root, k, path):
            if root.left != None:
                getKval(root.left, k, path)
            if len(path) == k:
                return
            path.append(root.val)
            if root.right:
                getKval(root.right, k, path)

        getKval(root, k, path)

        return path[-1]


if __name__ == "__main__":
    myT = treeTool.createBinaryTree([5,3,6,2,4,'#','#',1,'#'])
    a =Solution()
    print(a.kthSmallest(myT,3))
    print("Done!")






