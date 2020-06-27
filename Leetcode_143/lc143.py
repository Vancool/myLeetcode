# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        def reverseList(root):
            pre = None
            while root:
                tmp = root.next
                root.next = pre
                pre = root
                root = tmp
            return pre

        if head == None: return head
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        back = reverseList(slow.next)
        slow.next = None
        head = dummy.next
        while back:
            headtmp = head.next
            head.next = back
            backtmp = back.next
            back.next = headtmp
            head = headtmp
            back = backtmp
        return dummy.next
