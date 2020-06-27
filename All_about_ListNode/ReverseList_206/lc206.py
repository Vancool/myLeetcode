# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
方法一.原地扭转
'''
class Solution(object):
    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
'''
方法二. 假头扭转
'''
class Solution(object):
    def reverseList(self, head):
        dummy = ListNode(0)
        while head:
            tmp = dummy.next
            dummy.next = head
            head = head.next
            dummy.next.next = tmp
        return dummy.next

'''
方法三.使用栈
方法四.递归
'''
class Solution(object):
    def reverseList(self, head):
        def Helper(head):
            if head == None or head.next == None:
                return head, head
            pre, lastone = Helper(head.next)
            pre.next = head
            head.next = None
            return pre, head

        pre,_ = Helper(head)
        return pre


