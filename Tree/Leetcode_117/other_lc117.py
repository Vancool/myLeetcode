# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution(object):
    def connect(self, root):
        dummy = Node(0)
        cur = root
        tail = dummy
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
                cur = dummy.next # 下一层
                tail = dummy
                dummy.next = None #记得清空状态
        return root
