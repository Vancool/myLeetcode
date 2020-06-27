# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums: return None
        n = len(nums)
        root = TreeNode(nums[n//2])
        root.left = self.sortedArrayToBST(nums[:n//2])
        root.right = self.sortedArrayToBST(nums[n//2+1:])
        return root
