# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
https://leetcode-cn.com/problems/linked-list-cycle/solution/pythonti-jie-ha-xi-he-kuai-man-zhi-zhen-de-ai-qing/
还是不会，判断是否为环形链表

这题用快慢指针做
为什么快慢指针在环形链表中总是会相遇？
假设一个链表， 不在圈里面的有n个，在圈里面的有k个
当慢指针走完n步， 快指针走了2n，这个时候慢指针刚准备走到圈内，但是快指针早就在圈里走了
如果 k >= n 
说明快指针还没走完一圈， 快指针要和慢指针重合就肯定要走过一圈的，此时快慢指针的距离为 k-n
因为每次快指针都能缩短1格距离，所以以慢指针作为参考系，再经过k-n格就能追上慢指针与之重合
这种情况时间复杂度为 O（n + k- n） = O(k)

如果 k <= n
说明快指针至少走完了一圈，这个时候所在的位置是0 <= n % k < k
所以之后要再操作 k - n%k 次
时间复杂度为 O(n+k)
链表长度为 n+k

实际写法是 low = head
          fast = head.next
注意区分一下
 
'''
class Solution(object):
    def hasCycle(self, head):
        if head == None or head.next == None:
            return False
        low = head
        fast = head.next
        while low != fast:
            if fast.next == None or fast.next.next == None:
                return False
            low = low.next
            fast = fast.next.next
        return True
