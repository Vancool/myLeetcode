from Tree.Leetcode_297.Mycode import Codec
'''
中序遍历的改造，注意的是python的全局变量问题
这个题还可以改成return 最后一个节点，这样就可以不用声明global
'''
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        global pre,head
        pre = None
        head = None
        if root == None:
            return None
        def process(root):
            global pre,head

            if root.left:
               process(root.left)
            if pre == None:
               head = root
               pre = root
            else:
                pre.right = root
                root.left = pre
                pre = pre.right
            if root.right:
                process(root.right)
        process(root)
        head.left = pre
        pre.right = head
        return head

myT = Codec()
myT = myT.deserialize('[4,2,5,1,3]')
b = Solution()
head = b.treeToDoublyList(myT)
print("Done")
