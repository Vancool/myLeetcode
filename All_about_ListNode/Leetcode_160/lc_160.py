# Definition for singly-linked list.
from All_about_ListNode import getList
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        countA = 0
        countB = 0
        curA = headA
        curB = headB
        while curA:
            curA = curA.next
            countA += 1
        while curB:
            curB = curB.next
            countB += 1
        startA = headA
        startB = headB
        while countA > countB:
            countA -= 1
            startA = startA.next
        while countB > countA:
            countB -= 1
            startB = startB.next
        while startA and startB:
            if startB == startA:
                return startB
            startA = startA.next
            startB = startB.next
        return None





