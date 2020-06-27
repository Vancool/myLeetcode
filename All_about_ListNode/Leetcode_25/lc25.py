# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def reverseKGroup(self, head, k):
        if k == 1 or head == None: return head
        dummy = ListNode(0)
        dummy.next = head
        curdummy = dummy
        while head:
            tail = curdummy
            count = 0
            while tail and count < k:
                count += 1
                tail = tail.next
            if tail == None: break
            pre = tail.next
            end = tail.next
            nextdummy = head
            while head != end:
                tmp = head.next
                head.next = pre
                pre = head
                head = tmp
            curdummy.next = pre
            curdummy = nextdummy
            head = curdummy.next
        return dummy.next


'''
自己写得真是太乱了，导致了面试失败
看other
'''
from All_about_ListNode.getList import getList,printList
l = getList([1,2,3,4,5])
a = Solution()
l = a.reverseKGroup(l,3)
print(printList(l))

