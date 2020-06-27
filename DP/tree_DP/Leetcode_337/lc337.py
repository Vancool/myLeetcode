# Definition for a binary tree node.
from Tree.TreeTool.lc_297 import Codec
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        def Process(root, father_used):
            if root.left == None and root.right == None:
                if father_used:
                    return 0
                else:
                    return root.val
            if father_used:
                tmp1, tmp2 = 0, 0
                if root.left:
                    tmp1 = Process(root.left, False)
                if root.right:
                    tmp2 = Process(root.right, False)
                return tmp1 + tmp2
            else:
                if root.left and root.right:
                    leafTrue = Process(root.left, True) + Process(root.right, True) + root.val
                    leafFalse = Process(root.left, False) + Process(root.right,False)
                    return max(leafFalse, leafTrue)
                elif root.left:
                    leafTrue = Process(root.left, True) + root.val
                    leafFalse = Process(root.left, False)
                    return max(leafFalse, leafTrue)
                elif root.right:
                    leafTrue = Process(root.right, True) + root.val
                    leafFalse = Process(root.right, False)
                    return max(leafFalse, leafTrue)

        return Process(root, False)

'''
自己写的方法，递归调用 时间复杂度为 O(2 ** n) n为树的个数，虽然是对的但是超时了

可以用记忆递归，因为比如 
     A(根)
    B   C
   D E F G
只计算A-B-D这一条分支， 都会重复计算不用父亲的和用父亲时候得到的最大值，所以可以记录下子节点的不用重复计算（自己画个图，很好理解的）
因此可以用一个hashmap来记住已经走过的路
'''
class Solution(object):
    def rob(self, root):
        hashmapUsed = {}
        hashmapNotUsed={}
        def Process(root, father_used):
            if root == None:
                return 0
            if root.left == None and root.right == None:
                if father_used:
                    hashmapUsed[root] = 0
                    return 0
                else:
                    hashmapNotUsed[root] = root.val
                    return root.val
            if father_used:
                if root in hashmapUsed:
                    return hashmapUsed[root]
                tmp1 = Process(root.left, False)
                tmp2 = Process(root.right, False)
                hashmapUsed[root] = tmp1 + tmp2
                return tmp1 + tmp2
            else:
                if root in hashmapNotUsed:
                    return hashmapNotUsed[root]
                leafTrue = Process(root.left, True) + Process(root.right, True) + root.val
                leafFalse = Process(root.left, False) + Process(root.right,False)
                hashmapNotUsed[root] = max(leafTrue, leafFalse)
                return max(leafFalse, leafTrue)
        return Process(root, False)

'''
如何从记忆递归推到动态规划？
我们所知道的是每次递归只是父子之间，不需要保存这么多值，所以可以空间优化，那么怎么优化？
找一下边界条件，其实就是到叶子是边界
那么可以先从叶子算起 就是后序遍历，把叶子的用和不用算出来，从而算出父亲的用和不用，这样递归到上一层
（可以用递归返回一个数组表示叶子节点的用和不用的值， 不可以在外面放一个全局的数组，因为我们也不知道某一层的叶子有多少个，所以数组可能会爆掉

'''
class Solution(object):
    def rob(self, root):
        def Process(root):
            #这个时候就不用管父亲到底用不用，由孩子来决定，父亲用不用都会返回一个用/不用最大值数组
            #0 表示这个节点不用 1 表示这个节点用
            if root == None:
                return [0,0]
                '''这边一定要return [0,0] 而不是0'''
            #这个是到达叶子节点的边界条件，可以和父亲节点一起写的
            # if root.left == None or root.right == None:
            #     return [0, root.val]
            res = [0] * 2

            left = Process(root.left)
            right = Process(root.right)
            '''
            注意这边一定要用两个临时数组存着，不然每次调用都会递归到底
            '''
            res[0] = max(left[0], left[1]) + max(right[0], right[1])
            res[1] = left[0] + right[0] + root.val
            return res
        res = Process(root)
        return max(res)

'''
实际想想其实就是把每层的子节点用不用的情况求完，然后求上一层的后序遍历
'''

c = Codec()
tree = c.deserialize('[5,4]')
a = Solution()
print(a.rob(tree))
print("Done")
