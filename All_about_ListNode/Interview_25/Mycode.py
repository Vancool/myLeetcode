class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
from All_about_ListNode import getList
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 ==None:
            return l2
        if l2 == None:
            return l1
        head = ListNode(0)
        cur = head
        while l1 and l2:
            if l1.val <= l2.val:
                print('l1',l1.val)
                cur.next = l1
                l1 = l1.next
            else:
                print('l2',l2.val)
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # if l1:
        #     cur.next = l1
        # if l2:
        #     cur.next = l2
        cur.next = l1 if l1 else l2
        return head.next

l1 = [1,2,4]
l2 = [1,3,4]
l1 = getList.getList(l1)
l2 = getList.getList(l2)
a = Solution()
myList = a.mergeTwoLists(l1,l2)
print(getList.printList(myList))
print("Done")