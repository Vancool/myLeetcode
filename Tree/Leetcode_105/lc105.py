# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0: return None
        hashmap = {}
        hashmap2 = {}
        for i, num in enumerate(inorder):
            hashmap[num] = i
        for i, num in enumerate(preorder):
            hashmap2[num] = i
        def getTree(preleft, preright,preorder,inleft, inright,inorder):
            if preleft > preright:return None
            if inleft > inright:return None
            rootVal = preorder[preleft]
            root = TreeNode(rootVal)
            root_inorder_index = hashmap[rootVal]
            root.left = getTree(preleft + 1, preright, preorder, inleft, root_inorder_index-1, inorder)
            if root.left == None:
                right_preorder_index = preleft + 1
            else:
                left_last_val = inorder[root_inorder_index-1]
                right_preorder_index = hashmap2[left_last_val] + 1
            root.right =getTree(right_preorder_index, preright, preorder, root_inorder_index+1, inright, inorder)
            return root
        return getTree(0, len(preorder)-1, preorder,0, len(inorder)-1, inorder)


'''
这题我第二遍写，没写出来，只过了20个样例
'''

a = Solution()
pre = [3,2,1,4]
ino = [1,2,3,4]
tree = a.buildTree(pre, ino)
