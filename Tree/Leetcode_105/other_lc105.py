# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0: return None
        inorder_hashmap = {}
        for i, num in enumerate(inorder):
            inorder_hashmap[num] = i
        def buildTree(preleft, preright, inleft, inright):
            if preleft > preright or inleft > inright:
                return None
            root = TreeNode(preorder[preleft])
            root_inorder_index = inorder_hashmap[preorder[preleft]]
            left_num = root_inorder_index - inleft
            root.left = buildTree(preleft+1, preleft+1+left_num-1, inleft, root_inorder_index-1)
            root.right = buildTree(preleft+1+left_num,preright, root_inorder_index+1, inright)
            return root
        return buildTree(0, len(preorder)-1, 0, len(inorder)-1)


'''
如果用迭代可以进化成模拟前序遍历， 这个时候就需要有一个stop的value值来确定是否为叶子
看题解：
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--22/
模拟一个前序遍历的过程， 判断递归返回的叶子节点的方式是：

如果满足 preoder[pre] == inorder[in] 
对判断左子树是否直接返回本身结束递归只需要看它的父亲是否满足父子颠倒（preoder[pre-1] == inorder[in+1])
对判断右子树就需要找到很久远的祖先的值才能确定是否能够直接 return, 即(preorder[pre-n] == inorder[in+1] )
所以左子树递归传父亲值， 而右子树递归传祖先值。

'''