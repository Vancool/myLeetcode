# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        curdummy = dummy
        while curdummy:
            head = curdummy.next
            if not head or not head.next: break
            next = head.next
            head = next.next
            next.next = head
            curdummy.next = next
            curdummy = head
        return dummy.next

