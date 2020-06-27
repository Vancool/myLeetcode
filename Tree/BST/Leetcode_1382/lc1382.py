# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def balanceBST(self, root):
        if root == None:
            return None

        def right_right(root):
            tmp = root.right
            root.right = tmp.left
            tmp.left = root
            return tmp
        def left_left(root):
            tmp = root.left
            root.left = tmp.right
            tmp.right = root
            return tmp


        dummy = TreeNode(10^5+1)

'''
这题没写出来
其实就是先将搜索二叉树转化为有序数组， 然后将有序数组转化为平衡二叉树
这题可以先做 Leetcode 108
'''

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        inorder_list = []
        def get_inorder_list(root):
            if root == None: return
            get_inorder_list(root.left)
            inorder_list.append(root.val)
            get_inorder_list(root.right)
        def build_BST(nums, l, r):
            if not nums or l > r: return None
            mid = l + (r-l+1)>>2
            root = TreeNode(nums[mid])
            root.left = build_BST(nums, l, mid-1)
            root.right = build_BST(nums,mid+1, r)
            return root

        get_inorder_list(root)
        return build_BST(inorder_list, 0, len(inorder_list)-1)





