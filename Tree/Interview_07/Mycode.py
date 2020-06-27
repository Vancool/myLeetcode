# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        def treeHelper(preoder, nextIndex, inorder ):
            if len(inorder) == 0 or nextIndex>= len(preorder):
                return None
            if len(inorder) == 1:
                return TreeNode(inorder[0])
            root = TreeNode(preorder[nextIndex])
            for i in range(len(inorder)):
                if root.val == inorder[i]:
                    break
            leftInOrder = inorder[0:i]
            rightInOrder = inorder[i+1:len(inorder)]
            root.left = treeHelper(preorder, nextIndex+1,leftInOrder)
            root.right = treeHelper(preorder, nextIndex+1+len(leftInOrder), rightInOrder)
            return root

        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                break
        leftInOrder = inorder[0:i]
        rightInOrder = inorder[i+1:len(inorder)]
        root.left = treeHelper(preorder,1,leftInOrder )
        root.right = treeHelper(preorder, 1+len(leftInOrder),rightInOrder)
        return root

if __name__ == "__main__":
    a = Solution()
    tree = a.buildTree([-1],[-1])
    print("done")