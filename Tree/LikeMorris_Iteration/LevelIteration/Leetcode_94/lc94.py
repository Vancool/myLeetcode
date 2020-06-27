# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def inorderTraversal(self, root):
        self.res = []
        def Process(root):
            if root == None:
                return
            Process(root.left)
            self.res.append(root.val)
            Process(root.right)
        Process(root)
        return self.res

from Tree.TreeTool.lc_297 import Codec
class Solution(object):
    def inorderTraversal(self, root):
        if root == None:
            return []
        res = []
        stack = []
        stack.append(root)
        before = False
        while stack:
            while stack[-1].left and not before:
                stack.append(stack[-1].left)
                before = False

            root = stack.pop()
            res.append(root.val)
            if root.right and root.right:
                stack.append(root.right)
                before = False
            else:
                before = True
        return res

'''
自己写得迭代真的好乱，需要多加一个一个visited
事实上不需要这么写，可以判断要不要放到没到Null另一种写法：
'''
class Solution(object):
    def inorderTraversal(self, root):
        stack = []
        res = []
        cur = root
        while len(stack) > 0 or cur is not None:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                root = stack.pop() #而不是cur = stack.pop()，不然left会重复加入
                res.append(root.val)
                if root.right:
                    cur = root.right
        return res


'''
不破坏树结构的morris解法
'''
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        while root:
            if root.left:
                pre = root.left
                while pre.right and pre.right!= root:
                    pre = pre.right
                if pre.right is None:
                    pre.right = root
                    root = root.left
                else: # pre.right == root 此时已经搭好树了,需要把树拆掉
                    pre.right = None #原来是找到一个null节点把root装上
                    res.append(root.val)
                    root = root.right #走到这边的时候左边已经从下往上走完了，所以遍历右边
            else: # root.left == None
                res.append(root.val)
                root = root.right # 因为root.right 已经被转换成根了，所以不会是null
        return res



c = Codec()
myTree = c.deserialize('[1,null,2,3]')
a = Solution()
print(a.inorderTraversal(myTree))
print("Done")