# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        key = 0
        addVal = l1.val + l2.val + key
        if (addVal >= 10):
            addVal -= 10
            key = 1
        else:
            key = 0
        parent = ListNode(addVal)
        head.next = parent
        l1 = l1.next
        l2 = l2.next
        while (l1 and l2):
            addVal = l1.val + l2.val + key
            if (addVal >= 10):
                addVal -= 10
                key = 1
            else:
                key = 0
            parent.next = ListNode(addVal)
            parent = parent.next
            l1 = l1.next
            l2 = l2.next
        if (l1):
            parent.next = l1
            if(key):
                l1.val += key
                while(l1.val >= 10 ):
                    l1.val -= 10
                    if(l1.next):
                        l1 = l1.next
                        l1.val += 1
                    else:
                        l1.next = ListNode(1)
                key = 0

        if (l2):
            parent.next = l2
            if(key):
                l2.val += key
                while(l2.val >= 10):
                    l2.val -= 10
                    if(l2.next):
                        l2 = l2.next
                        l2.val += 1
                    else:
                        l2.next = ListNode(1)
                key = 0

        if(key):
            parent.next = ListNode(key)
        return head.next

if __name__ == "__main__":
    a = Solution( )
    l1 = ListNode(9)
    l1.next = ListNode(9)
  #  l1.next.next = ListNode(3)
    l2 = ListNode(1)
  #  l2.next = ListNode(6)
    print(a.addTwoNumbers(l1, l2))