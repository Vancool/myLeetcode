# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        if head == None:
            return None
        has_seen = set()
        while head is not None and head not in has_seen:
            has_seen.add(head)
            head = head.next
        return head if head in has_seen else None