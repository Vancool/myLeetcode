from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        if root == None:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            res.append(queue[-1].val)
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res

'''
如果自己想要用深搜请认真设计深搜的顺序！
可以用深搜！！
这一题是 [根， 右， 左]
如何判断要不要输出左边呢？ 记录一个深度看 res[深度]是否已经有数值了
因为 res是全局变量所以会一找到就填上，而 depth必须是局部变量只是记录某个节点在哪一层
因为是一个深度一个坑的
'''

class Solution(object):
    def rightSideView(self, root):
        res = []
        def dfs(root, depth):
            if root == None:
                return
            if depth == len(res):
                res.append(root.val)
            depth += 1
            dfs(root.right, depth)
            dfs(root.left, depth)
        dfs(root, 0)
        return res




'''
自己写的深搜没过
比如
test case [1,2,3,4]
  1 
 2 3
4 
'''