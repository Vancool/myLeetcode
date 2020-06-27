'''

这个是直接层次遍历，然后层次遍历完后直接反转需要逆着遍历的层的节点
'''
class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        nodeStack=[pRoot]
        result=[]
        while nodeStack:
            res = []
            nextStack=[]
            for i in nodeStack:
                res.append(i.val)
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
            nodeStack=nextStack
            result.append(res)
        returnResult=[]
        for i,v in enumerate(result):
            if i%2==0:
                returnResult.append(v)
            else:
                returnResult.append(v[::-1])
        return returnResult