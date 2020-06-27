
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

'''
这份代码是错的，这道题不能用递归来做
'''
class Solution(object):
    def connect(self, root):
        if root == None:
            return
        if root.left and root.right:
            root.left.next = root.right
        if root.right and root.next:
            if root.next.left:
                root.right.next = root.next.left
            elif root.next.right:
                root.right.next = root.next.right
        elif root.left and root.next:
            if root.next.left:
                root.left.next = root.next.left
            elif root.next.right:
                root.left.next = root.next.right
        if root.left:
            self.connect(root.left)
        if root.right:
            self.connect(root.right)
        return root
'''
用116的迭代方法做的
特别不优雅，可以看others的双链表模拟队列解法
'''
class Solution(object):
    def connect(self, root):
        if root == None: return None
        node = root
        while node:
            cur = node
            while cur:
                if cur.left and cur.right:
                    cur.left.next = cur.right
                pre = None
                if cur.right:
                    pre = cur.right
                elif cur.left:
                    pre = cur.left
                nx = cur.next
                while nx and pre:
                    if nx.left:
                        pre.next = nx.left
                        break
                    elif nx.right:
                        pre.next = nx.right
                        break
                    else:
                        nx = nx.next
                cur = cur.next
            while node and not node.left and not node.right:
                node = node.next
            if not node: break
            if node.left:
                node = node.left
            else:
                node = node.right
        return root
