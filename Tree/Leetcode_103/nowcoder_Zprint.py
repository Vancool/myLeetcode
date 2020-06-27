# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from Tree import treeTool
from collections import deque
class Solution:
    def Print(self, pRoot):
        if pRoot == None:
            print([])

        levelRes = deque()
        preNodeStack = deque()
        curNodeStack = deque()
        preNodeStack.append(pRoot)
        res = deque([[pRoot.val]])
        level = 1
        while len(preNodeStack)>0 or len(curNodeStack)>0:
            if level&1 == 1:
                curNode = preNodeStack.pop()
                if curNode.right:
                    levelRes.append(curNode.right.val)
                    curNodeStack.append(curNode.right)
                if curNode.left:
                    levelRes.append(curNode.left.val)
                    curNodeStack.append(curNode.left)
                if len(preNodeStack) == 0 and len(curNodeStack)> 0:
                    res.append(levelRes)
                    level += 1
                    levelRes = deque()
            else:
                curNode = curNodeStack.pop()
                if curNode.left:
                    levelRes.append(curNode.left.val)
                    preNodeStack.append(curNode.left)
                if curNode.right:
                    levelRes.append(curNode.right.val)
                    preNodeStack.append(curNode.right)
                if len(preNodeStack) > 0 and len(curNodeStack)== 0:
                    res.append(levelRes)
                    level += 1
                    levelRes = deque()
        print(res)

myTree = treeTool.createBinaryTree([8,6,10,5,7,9,11])
a = Solution()
a.Print(myTree)
print("Done!")


