from All_about_ListNode.getList import getList
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
不会做
原来是用快慢指针找到中间节点
然后从中间节点开始反转后面一半的链表
然后两个指针 一个指向头 一个指向中间+1 
'''
class Solution(object):
    def isPalindrome(self, head):
        if head == None or head.next == None:
            return True
        midNode = self.find_mid(head)
        secondhead = self.reverseList(midNode.next)
        res = True
        while res and head is not None and secondhead is not None:
            res = (head.val == secondhead.val)
            head = head.next
            secondhead = secondhead.next
        return res
    def reverseList(self, head):
        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def find_mid(self,head):
        #这个函数能够拿到偶数节点的前一半
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

a = Solution()
s = getList([1,1,2,1])
print(a.isPalindrome(s))
print("Done")

