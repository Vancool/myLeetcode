# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
后序遍历

'''

#递归解法
class Solution(object):
    def postorderTraversal(self, root):
        res = []
        def recur(root):
            if root == None:
                return
            recur(root.left)
            recur(root.right)
            res.append(root.val)
        recur(root)
        return res
'''
栈解法
1.逆序 左右根 变成 根右左
'''
class Solution(object):
    def postorderTraversal(self, root):
        if root == None: return []
        res = []
        stack = []
        stack.append(root)
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return res[::-1]

'''
2. 判断元素折回来的还是在继续深入 append 孩子的方法：
 可以用一个 set 记录到之前是否有碰到
 另一种记录方法：
栈里面append两个数一个之后输出数一个用来迭代
如何判断到底是折回来的还是继续往下 append 孩子： 用root == stack.peek()判断
'''
class Solution(object):
    def postorderTraversal(self, root):
        if root == None:
            return []
        res = []
        stack = [root, root]
        while stack:
            root = stack.pop()
            if len(stack) > 0 and root == stack[-1]:
                if root.right:
                    stack.append(root.right)
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
                    stack.append(root.left)
            else:
                res.append(root.val)
        return res

'''
3. 中序遍历
不用单独开个空间看看是否是折回来的
只要记录一个前一次循环遍历的指针 pre， 看root.right 是不是pre
这样就可以不用那么早 pop掉根了
'''
class Solution(object):
    def postorderTraversal(self, root):
        if root == None: return []
        res = []
        stack = []
        pre = None
        while root or stack:
            if root:
                while root:
                    stack.append(root)
                    root = root.left
            else:
                root = stack[-1]
                if root.right == None or root.right == pre:
                    res.append(root.val)
                    pre = root
                    stack.pop()
                    root = None
                else:
                    root = root.right
        return res

