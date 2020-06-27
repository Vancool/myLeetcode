from Tree.Leetcode_297.Mycode import Codec
'''
这题没写出来
'''
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None or (not root.left and not root.right):
            return root
        def getNode(root, is_left):
            if is_left :
                curRoot = root.left
            else:
                curRoot = root.right
            if curRoot == None:
                return
            if curRoot.left:
                curLeft = curRoot.left
                if curLeft.right == None:
                    curLeft.right = curRoot
                else:
                    getNode(curRoot, is_left)
                if curLeft.left == None:
                    if not is_left:
                        curLeft.left = root
                else:
                    getNode(curRoot, is_left)
            else:
                if not is_left:
                    curRoot.left = root
            if curRoot.right:
                curRight = curRoot.right
                if curRight.left == None:
                    curRight.left = curRoot
                else:
                    getNode(curRoot, not is_left)
                if curRight.right == None:
                    if is_left:
                        curRight.right = root
                else:
                    getNode(curRoot, not is_left)
            else:
                if is_left:
                    curRoot.right = root

        if root.left:
            getNode(root,True)
        if root.right:
            getNode(root, False)
        cur = root
        head = cur
        while cur.left:
            cur = cur.left
            head = cur
        cur = root
        tail = cur
        while cur.right:
            cur = cur.right
            tail = cur
        tail.right = head
        head.left = tail
        return head

myT = Codec()
myT = myT.deserialize('[4,2,5,1,3]')
b = Solution()
head = b.treeToDoublyList(myT)
print("Done")

