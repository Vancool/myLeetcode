# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        # if root == None:
        #     return 0
        self.res = 0
        def Process(root):
            if root == None:
                return 0
            left = Process(root.left)
            right = Process(root.right)
            self.res = max(left+right+root.val, self.res, max(right, left,0) + root.val)
            return max(right, left,0) + root.val
        Process(root)
        return self.res


'''
test case:
[1,-2,3]
'''