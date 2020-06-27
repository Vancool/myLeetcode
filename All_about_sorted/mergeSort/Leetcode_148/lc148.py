# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        def merge(listA, listB):
            if listA == None: return listB
            if listB == None: return listA
            dummy = ListNode(0)
            cur = dummy
            while listA and listB:
                if listA.val <= listB.val:
                    cur.next = listA
                    listA = listA.next
                else:
                    cur.next = listB
                    listB = listB.next
                cur = cur.next
            if listA: cur.next = listA
            if listB: cur.next = listB
            return dummy.next
        if head == None: return head
        num = 0
        cur = head
        while cur:
            num += 1
            cur = cur.next
        dummy = ListNode(0)
        dummy.next = head
        count = 1
        while count <= num:
            curdummy = dummy
            while curdummy and curdummy.next:
                i = 0
                mid = curdummy
                fast = curdummy
                while i < count and fast and fast.next:
                    mid = mid.next
                    fast = fast.next.next
                    i += 1
                if fast and i >= count:
                    next_start = fast.next
                    fast.next = None
                    midstart = mid.next
                    mid.next = None
                    curdummy.next = merge(curdummy.next, midstart)
                    while curdummy.next:
                        curdummy = curdummy.next
                    curdummy.next = next_start
                else:
                    i = 0
                    cur = curdummy
                    while i < count and cur:
                        i += 1
                        cur = cur.next
                    if cur == None: break
                    start = cur.next
                    cur.next = None
                    curdummy.next = merge(curdummy.next, start)
                    curdummy = None
            count *= 2
        return dummy.next
'''
这一题我自己写的时候写得还是有点乱，还是要模块化比较好

原理都是归并排序
'''


class Solution(object):
    def sortList(self, head):
        if head == None or head.next == None: return head
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        count = 1
        dummy = ListNode(0)
        dummy.next = head
        while count < length:
            pre = dummy
            while pre:
                h1 = pre.next
                cur = pre.next
                i = 0
                while i < count and cur:
                    i += 1
                    cur = cur.next
                if cur == None:
                    pre = None
                    break
                h2 = cur
                i = 0
                while i < count and cur:
                    i += 1
                    cur = cur.next
                c1,c2 = 0,0
                while c1 < count and c2 < i:
                    if h1.val <= h2.val:
                        pre.next = h1
                        h1 = h1.next
                        c1 += 1
                    else:
                        pre.next = h2
                        h2 = h2.next
                        c2 += 1
                    pre = pre.next
                while c1 < count:
                    pre.next = h1
                    h1 = h1.next
                    pre = pre.next
                    c1 += 1
                while c2 < i:
                    pre.next = h2
                    h2 = h2.next
                    pre = pre.next
                    c2 += 1
                pre.next = cur
            count *= 2
        return dummy.next





from All_about_ListNode.getList import getList,printList

myList = getList([3,2,1])
a = Solution()
myList = a.sortList(myList)
printList(myList)






