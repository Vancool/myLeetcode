# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
这题和 Leetcode 105 类似
'''
class Solution(object):
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        inorderhash ={}
        for i, num in enumerate(inorder):
            inorderhash[num] = i
        def getTree(postIndex, inleft, inright):
            if postIndex < 0 or inleft > inright:
                return None
            root = TreeNode(postorder[postIndex])
            root_inorder_index = inorderhash[postorder[postIndex]]
            rightnum = inright - root_inorder_index
            root.right = getTree(postIndex-1, root_inorder_index+1,inright)
            root.left = getTree(postIndex-1-rightnum, inleft, root_inorder_index-1)
            return root
        return getTree(len(postorder)-1, 0, len(inorder)-1)



class Solution(object):
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        self.post = len(postorder)-1
        self.ino = len(inorder) - 1
        def getTree(value):
            if self.post < 0 or self.ino < 0:
                return None
            if inorder[self.ino] == value:
                self.ino -= 1
                return
            root = TreeNode(postorder[self.post])
            self.post -= 1
            root.right = getTree(root.val)
            root.left = getTree(value)
            return root
        root = getTree(float('inf'))
        return root
