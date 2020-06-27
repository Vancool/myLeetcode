
'''
中序遍历的非递归方法，使用stack

'''
from Tree import treeTool
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution(object):
    def kthSmallest(self, root, k):
        if root == None or k == 0:
            return None

        stack = deque()
        count = 0
        stack.append(root)
        curNode = root
        is_not_use = True
        while  len(stack)>0:
            while curNode is not None:
                while curNode.left and is_not_use:
                    stack.append(curNode.left)
                    curNode = curNode.left
                curNode = stack.pop()
                #可能最后pop到空都没有找到，所以要加一个大于0来防止报错
                count += 1
                is_not_use = False
                if count == k:
                    return curNode.val
                if curNode.right:
                    stack.append(curNode.right)
                    curNode = curNode.right
                    is_not_use = True
        if count < k:
            return None

if __name__ == "__main__":
    myT = treeTool.createBinaryTree([5,3,6,2,4,'#','#',1,'#'])
    a =Solution()
    print(a.kthSmallest(myT,3))
    print("Done!")