
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

'''
解题思路为 求解两种不同的next的构造方式
'''
'''
递归解法
'''
class Solution(object):
    def connect(self, root):
        if root == None: return root
        if root.left:
            root.left.next = root.right
            '''这条判断语句是在有root.left的基础上的，如果有root.left才会有root.right'''
            if root.next: root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

'''
迭代解法
其实就是一种另类的层次遍历
'''
class Solution(object):
    def connect(self, root):
        if root == None: return root
        cur = root
        while cur.left:
            pre = cur
            while pre:
                pre.left.next = pre.right
                if pre.next:
                    pre.right.next = pre.next.left
                pre = pre.next
            cur = cur.left
        return root

'''
双链表模拟层次遍历
'''
class Solution(object):
    def connect(self, root):
        dummy = Node(0)
        tail = dummy
        cur = root
        while cur:
            if cur.left:
                tail.next = cur.left
                tail = tail.next
            if cur.right:
                tail.next = cur.right
                tail = tail.next
            if cur.next:
                cur = cur.next
            else:
                cur = dummy.next
                dummy.next = None
                tail = dummy
        return root


