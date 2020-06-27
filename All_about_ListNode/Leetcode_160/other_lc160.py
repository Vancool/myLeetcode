class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

'''
超级巧妙地用拼接链表的方法来做求出A链表和B链表的长度差
假设 A = [a+c]
     B = [b+c]
c 是后面相同部分的元素，两个拼在一起一起走就是：
  A + B ：[(a+c)+(b+c)]
  B + A ：[(b+c)+(a+c)]
  那么走完A走B走到 a+c+b段
  走完B走A走到     b+c+a段
  就开始相遇了！！
  其实如果是求差的话，假设A比较长
  走 A + B 走到 A 的时候， 走B+A段的指针刚好走到 B+A的一部分
  这样的话就能够得到A比B长的部分了
  就是很神奇hhhh
'''


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA = headA
        pB = headB
        while pA != pB:
            '''if 不要写pA.next
            因为pA 和 pB 不会同时为null(同时为null就退出了)
            所以只要检测pA是不是null或者pB是不是null就好了
            如果检测pA.next会一直只要是null变为headB没有交点跳不出循环

            continue是要再比一次，因为前面是和null在比
            但是不能写continue，因为前面如果变成next就错位了
            可以直接不写continue 因为 两段的null都会在找到节点之前比一次，可以抵消了
            '''
            if pA:
                pA = pA.next
            else:
                pA = headB
            if pB:
                pB = pB.next
            else:
                pB = headA
        return pA

'''
如果是我的想法我会考虑null
我是这么写的：
'''
class Solution2(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pA = headA
        pB = headB
        while pA or pB:
            if pA == None:
                pA = headB
            elif pB == None:
                pB = headA
            if pA == pB:
                return pA
            pA = pA.next
            pB = pB.next
        return None