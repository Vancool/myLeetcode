# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
https://leetcode-cn.com/problems/linked-list-cycle-ii/ 
环形链表 II

链表 a+b （a+1为入口处）
先找环
找到环之后根据式子可以计算出 slow = nb    
                          fast = 2nb
所以此时假设从head 走a步可以到圈的第一个节点
那么
'''
class Solution(object):
    def detectCycle(self, head):
        if head == None:
            return None
        fast, slow = head, head
        while True:
            if fast.next is None or fast.next.next is None: return None
            fast = fast.next.next
            slow = next.next
            if slow == fast:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast

