# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
我自己写的话就会先求一个高度树然后从顶到低判断
但是其实可以将True / False作为全局变量来做
模板其实还是求高度的那个模板
或者是将False看成一个肯定不会出现的高度比如 -1只要判断顶部是-1就是False
'''
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = True
        if root == None:
            return True
        def Helper(root):
            if root is None or not self.res:
                return 0
            leftNum = Helper(root.left)
            rightNum = Helper(root.right)
            if abs(leftNum-rightNum) > 1:
                self.res = False
            return max(rightNum, leftNum) + 1
        Helper(root)
        return self.res
