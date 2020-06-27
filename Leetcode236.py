class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parentStack = []
        cur = root
        self.getParentStack(root, parentStack)
        # print(parentStack)
        parentStack = parentStack[::-1]
        for parent in parentStack:
            # print(parent)
            if (self.findNode(parent, p) and self.findNode(parent, q)):


                return parent.val

        return -1  # cannot find parent

    def findNode(self, root, p):
        if (root != None):
            if (root.val == p):

                return True
            if (self.findNode(root.left, p) or self.findNode(root.right, p)):

                return True
        return False

    def getParentStack(self, root, stack):
        if (root != None):
            stack.append(root)

            self.getParentStack(root.left, stack)
            self.getParentStack(root.right, stack)
if __name__ =="__main__":
    a = Solution()

    root = TreeNode(3)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    #print(a.findNode(root, 6))
    #print(a.findNode(root, 5))
    print(a.lowestCommonAncestor(root,5,1))

