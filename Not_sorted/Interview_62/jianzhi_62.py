class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
'''
自己写了个环形链表模拟
超时了
复杂度为O(m*n)
约瑟夫问题，有公式
'''
class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return n-1
        '''
        用一个环形链表模拟
        '''
        i = 0
        cur = Node(i)
        head = cur
        while i < n-1:
            cur.next = Node(i+1)
            cur = cur.next
            i += 1
        par = cur
        cur.next = head
        count = 0
        cur_n = n
        cur = head
        while count < n:
            step = int((m-1)% cur_n)
            '''parent 一定要在循环外assign，不然如果step = 0 就没东西可以删了'''
            while step:
                par = cur
                cur = par.next
                step -= 1
            #delete the Node
            #print(cur.val)
            par.next = cur.next
            cur = par.next
            cur_n -= 1
            count += 1
        return cur.val

a = Solution()
print(a.lastRemaining(6, 7))
print("Done")




