class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-2-7/
自己是想用记忆递归来写，感觉内存会爆掉
所以最终还是看别人的优化

解法一.
求出 [1,2] [1,2,3] [1,2,3,4] 等等集合的树存起来，然后算右边的树时候克隆，然后加个偏置加速
但是大的算法框架还是递归

克隆的方法

解法二. 
树的结构的 动态规划
比如插入3 的时候，其实是最后成为 [1,2] 构造的树的头头，或者是第一个右孩子，第二个右孩子...
因此只要遍历所有的插入方式存起来就能得到n的
'''
class Solution1(object):
    def cloneTree(self, node, offset):
        if node == None: return None
        root = TreeNode(node.val + offset)
        root.left = self.cloneTree(node.left, offset)
        root.right = self.cloneTree(node.right, offset)
        return root

    def generateTrees(self, n):
        if n == 0: return []
        if n == 1: return [ TreeNode(1)]
        dp = [[] for _ in range(n+1) ]
        dp[0] = [None]
        dp[1] = [TreeNode(1)]
        for i in range(2,n+1):
            for rootIndex in range(1,i+1):
                # left, right 都是节点数量
                left = rootIndex -  1
                right = i - rootIndex
                offset = rootIndex
                for leftTree in dp[left]:
                    for rightTree in dp[right]:
                        root = TreeNode(rootIndex)
                        root.left = leftTree
                        root.right = self.cloneTree(rightTree, offset)
                        dp[i].append(root)
        return dp[n]


class Solution(object):
    def copyTree(self, node):
        if node == None: return None
        root = TreeNode(node.val)
        root.left = self.copyTree(node.left)
        root.right = self.copyTree(node.right)
        return root

    def generateTrees(self, n):
        if n == 0: return []
        if n == 1: return [ TreeNode(1)]

        dp = [[] for _ in range(n+1)]
        dp[0] = [None]
        dp[1] = [TreeNode(1)]
        for i in range(2, n+1):
            for tree in dp[i-1]:
                root = TreeNode(i)
                root.left = tree
                dp[i].append(self.copyTree(root)) #不copy的话可能等下改tree的结构会有问题
                root.left = None
                pre = tree
                while pre:
                    cur = pre.right
                    pre.right = root
                    root.left = cur
                    dp[i].append(self.copyTree(tree))
                    #copy完后改回来
                    pre.right = cur
                    pre = cur
                    root.left = None
        return dp[n]


'''
可以优化一下空间
'''
class Solution(object):
    def copyTree(self, node):
        if node == None: return None
        root = TreeNode(node.val)
        root.left = self.copyTree(node.left)
        root.right = self.copyTree(node.right)
        return root

    def generateTrees(self, n):
        if n == 0: return []
        if n == 1: return [ TreeNode(1)]

        stack = [TreeNode(1)]
        res = []
        for i in range(2, n+1):
            res = []
            for tree in stack:
                root = TreeNode(i)
                root.left = tree
                res.append(self.copyTree(root)) #不copy的话可能等下改tree的结构会有问题
                root.left = None
                pre = tree
                '''
                如果这边改成 pre = self.copyTree(tree) 就不用重新调整过来了
                '''
                while pre:
                    cur = pre.right
                    pre.right = root
                    root.left = cur
                    res.append(self.copyTree(tree))
                    #copy完后改回来
                    pre.right = cur
                    pre = cur
                    root.left = None
            stack = res
        return res




a = Solution()
a.generateTrees(3)
print("Done")





