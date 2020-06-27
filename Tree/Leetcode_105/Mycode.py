class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
自己写的算法其实思想已经和最优解法差不多
如果每次找index的时候用一个hashmap维护可能会更好
'''
class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        def getTree(preorder, inorder, preStart, inStart, inEnd, map):
            if preStart >= len(preorder):
                return None
            if inStart == inEnd:
                return TreeNode(inorder[inStart])
            root = TreeNode(preorder[preStart])
            k = map[preorder[preStart]]
            leftEnd = k-1
            leftNum = leftEnd-inStart+1
            rightStart = k+1
            rightNum = inEnd - rightStart+1
            if leftNum>0:
                root.left = getTree(preorder, inorder, preStart+1, inStart, leftEnd, map)
            if rightNum>0:
                root.right = getTree(preorder, inorder, preStart+max(leftNum,0)+1, rightStart, inEnd, map)
            return root
        n = len(preorder)
        '''
        此处将循环换成hashmap,否则最差时间复杂度为O(n^2)
        enumerate函数是index, val对，先出index再出val，然后字典里的形式是val:index
        '''
        map = {val:index for index, val in enumerate(inorder, start=0) }
        root = getTree(preorder, inorder, 0,0,n-1, map)
        return root

a = Solution()
tree = a.buildTree([3,9,20,15,7] ,[9,3,15,20,7])
print("Done")
