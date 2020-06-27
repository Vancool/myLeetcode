# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeDuplicateNodes(self, head):
        if not head: return head
        hashmap = set()
        cur = head
        parent = None
        while cur:
            if cur.val in hashmap:
                parent.next = cur.next
                cur = cur.next
                continue
            hashmap.add(cur.val)
            parent = cur
            cur = cur.next
        return head
