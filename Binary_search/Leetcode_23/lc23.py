# Definition for singly-linked list.
from All_about_ListNode.getList import getList,printList
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            l1 = lists[0]
            l2 = lists[1]
            dummy = ListNode(0)
            cur = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
            return dummy.next
        else:
            l1 = self.mergeKLists(lists[0: len(lists)//2+1])
            l2 = self.mergeKLists(lists[len(lists)//2+1:])
            return self.mergeKLists([l1, l2])


a = Solution()
l = [[1,4,5],[1,3,4],[2,6]]
Llist = [getList(i) for i in l]
print(printList(a.mergeKLists(Llist)))
print("Done")

'''
学习一下 Priority Queue的用法
我发现如果其实优先级并不是只比第一个
'''
from queue import PriorityQueue

pq = PriorityQueue()

pq.put((-1, 1) )
pq.put((-2, 2) )
pq.put((-3, 'b') )
pq.put((-3, 'a'))
pq.put((-3, 'c'))
pq.put((-3, 'd'))
while not pq.empty():
	print(pq.get() )

