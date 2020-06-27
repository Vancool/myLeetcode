# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from Tree.TreeTool.lc_297 import Codec
class Solution(object):
    def findMode(self, root):
        def process(root):
            if root == None:
                return
            self.dict = {}
            res = []
            process(root.left)
            self.dict[root.val] = self.dict.get(root.val, 0) + 1
            process(root.right)
        process(root)
        maxVal = 0
        for key, val in self.dict.items():
            if val == maxVal: res.append(key)
            elif val > maxVal:
                res = [key]
                maxVal = val
        return res

class Solution(object):
    def findMode(self, root):
        self.res = []
        self.pre = -1
        self.count = 0
        self.cur_count = 0

        def Process(root):
            if root == None: return
            Process(root.left)
            if self.pre == root.val:
                self.cur_count += 1
            else:
                self.cur_count = 1
                self.pre = root.val
            if self.count == self.cur_count:
                self.res.append(root.val)
            elif self.cur_count > self.count:
                self.count = self.cur_count
                self.res = [root.val]
            Process(root.right)
        Process(root)
        return self.res

class Solution(object):
    def findMode(self, root):
        if root == None: return []
        cur = root
        max_count = 0
        cur_count = 0
        pre = -float('inf')
        res = []
        while cur:
            if cur.left:
                root = cur.left
                while root.right and root.right != cur:
                    root = root.right
                if root.right == None:
                    root.right = cur
                    cur = cur.left
                else:
                    root.right = None
                    if pre == cur.val: cur_count += 1
                    else: cur_count = 1
                    pre = cur.val

                    if cur_count == max_count and cur_count != 0: res.append(cur.val)
                    if cur_count > max_count:
                        res = [cur.val]
                        max_count = cur_count
                    cur = cur.right
            else:
                if pre == cur.val:
                    cur_count += 1
                else:
                    cur_count = 1
                pre = cur.val
                if cur_count == max_count and cur_count!= 0: res.append(cur.val)
                if cur_count > max_count:
                    res = [cur.val]
                    max_count = cur_count
                cur = cur.right
        return res
c = Codec()
tree = c.deserialize('[0,null,0]')
a = Solution()
print(a.findMode(tree))
