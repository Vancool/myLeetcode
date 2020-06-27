# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverseKGroup(self, head, k):
        def reverseNode(head):
            pre = None
            cur = head
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre
        if head == None or k == 1: return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy #反转链表的伪头
        end = dummy #反转链表的最后一个
        while end.next:
            count = 0
            while end and count < k:
                end = end.next
                count += 1
            if end == None:
                break
            start = pre.next
            next_start = end.next
            end.next = None
            '''
            这个置为null可以方便reverseNode里面的判断
            如果不置null 需要在reverseNode里面加一个是否到达 end.next的操作
            要把 end.next也一起传进去
            '''
            reversehead = reverseNode(start)
            pre.next = reversehead
            start.next = next_start #注意这边变成了start.next
            pre = start
            end = start

        return dummy.next

from All_about_ListNode.getList import getList,printList
l = getList([1,2,3,4,5])
a = Solution()
l = a.reverseKGroup(l,3)
print(printList(l))








