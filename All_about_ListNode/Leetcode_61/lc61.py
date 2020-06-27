class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution(object):
    def rotateRight(self, head, k):
        if not head: return head
        list_len = 0
        cur = head
        while cur:
            list_len += 1
            cur = cur.next
        if k >= list_len: k = int(k % list_len)
        dummy = Node(-1)
        dummy.next = head
        fast, slow = dummy, dummy
        while k and fast:
            k -= 1
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        if slow.next == None: return head
        newhead = slow.next
        slow.next = None
        fast.next = head
        return newhead


