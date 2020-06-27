# Definition for a binary tree node.
from Tree.TreeTool.lc_297 import Codec
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        if root == None: return None
        if root.left is None:
            root.right = self.flatten(root.right)
            return root
        left = self.flatten(root.left)
        tmp = self.flatten(root.right)
        root.left = None
        root.right = left
        tail = left
        while tail.right:
            tail = tail.right
        tail.right = tmp
        return root


'''
我认为原地算法的空间复杂度为 O(1),是算上系统栈的的解法不是原地解法
因此需要用循环自顶向下改变
做一个类似于 mirroirs 算法, 从顶向下把左边移到右边
我自己写的是一个自底向上左边移到右边
'''

class Solution(object):
    def flatten(self, root):
        while root:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
        return root
'''
如果用递归解法还可以用后序遍历的方法
后序遍历 右左根 全局变量保存上次递归的root
就是保存上次递归的root变量next_one 
'''
class Solution(object):
    def flatten(self, root):
        self.next_one = None
        def helper(root):
            if root == None: return None
            helper(root.right)
            helper(root.left)
            root.left = None
            root.right = self.next_one
            self.next_one = root
        return helper(root)
a = Solution()
tool = Codec()
tree = tool.deserialize('[1,2,5,3,4,null,6]')
print(tool.serialize(a.flatten(tree)))

