# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
这题不难，可以用倒着中序遍历[右根左]来做，可以提前结束遍历不用全遍历完
'''
class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []

        def get_arr(root):
            if root.left:
                get_arr(root.left)
            res.append(root.val)
            if root.right:
                get_arr(root.right)
        get_arr(root)
        return res[-k]


