class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        output = ListNode(0)
        cur = head.next
        head.next = output.next
        output.next = head

        while (cur != None):

            a = cur.next
            cur.next = output.next
            output.next = cur

            cur = a

        return output.next

if __name__ == "__main__":
    a = Solution( )
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    print(a.reverseList(l1))