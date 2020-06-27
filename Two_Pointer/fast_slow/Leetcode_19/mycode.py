# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
1.很巧妙地用双指针找尾部倒数的节点（一开始的指针指到尾部的话与后一个指针相隔n）
2.用一个头指针来作为头部的父节点，这样就不用另外讨论了
'''
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n):
            first = first.next
        if first.next:
            second = second.next
            first = first.next
        second.next = second.next.next
        return dummy.next


