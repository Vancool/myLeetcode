# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        def Process(root, maxval, minval):
            if root == None: return True
            if root.val >= maxval or root.val <= minval:
                return False
            if root.left:
                if not Process(root.left,min(maxval, root.val) , minval)\
                        or root.left.val >= maxval \
                        or root.left.val >= root.val:
                    return False
            if root.right:
                if not Process(root.right, maxval, max(root.val, minval))\
                        or root.right.val <= minval \
                        or root.right.val <= root.val:
                    return False
            return True
        maxval = float('inf')
        return Process(root, maxval, - maxval)
'''
注意root 也要比右孙子小， 比左孙子大， 不能只关心局部
比如： [10,5,15,null, null,6，20 ]
'''

'''
自己的写法不好， 看others
'''
from Tree.TreeTool.lc_297 import Codec
a = Solution()
b = Codec()
tree = b.deserialize("[10,5,15,null,null,6,20]")
print(a.isValidBST(tree))
