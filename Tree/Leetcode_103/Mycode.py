from Tree import treeTool


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        nodeList1 = []
        nodeList2 = []
        res = []
        levelRes = []
        level = 1 #当level为偶数从左往右，奇数从右往左
        res.append([root.val])
        nodeList1.append(root)
        Pre_num = 1 #用来表示结束的标识符
        while len(nodeList2)>0 or len(nodeList1)>0: #说明上层是有节点的
            if level & 1 == 1: #从右往左
                curNode = nodeList1.pop()
                if curNode.right:
                    levelRes.append(curNode.right.val)
                    nodeList2.append(curNode.right)
                if curNode.left:
                    levelRes.append(curNode.left.val)
                    nodeList2.append(curNode.left)
                if len(nodeList1) == 0:
                    level += 1
                    if len(levelRes) > 0:
                        res.append(levelRes)
                    levelRes = []
            else: #从左往右
                curNode = nodeList2.pop()
                if curNode.left:
                    levelRes.append(curNode.left.val)
                    nodeList1.append(curNode.left)
                if curNode.right:
                    levelRes.append(curNode.right.val)
                    nodeList1.append(curNode.right)
                if len(nodeList2) == 0:
                    level += 1
                    if len(levelRes) > 0:
                        res.append(levelRes)
                    levelRes = []


        return res
myTree = treeTool.createBinaryTree([1,2,3,4,'#',"#",5])
a = Solution()
res = a.zigzagLevelOrder(myTree)
print("Done!")


