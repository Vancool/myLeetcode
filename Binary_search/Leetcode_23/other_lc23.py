from queue import PriorityQueue
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
Lc 23题
3种写法：
1. k个一组堆排序选最小 log(k) * N 
注意的是python3 和 python2 优先队列的写法
2.二分合并 （递归版和循环版） log(k) * N
提醒一下循环版不用额外空间，我自己写的是递归版还写的很冗余
'''

class Solution1(object):
    def mergeKLists(self, lists):
        qp = PriorityQueue()
        for i, l in  enumerate(lists):
            if l != None:
                qp.put((l.val,i, l))
                '''Python3 写法 from queue import PrioirityQueue
                优先级并不是只比第一个，而是逐级比下去的
                如果后面有一个无法比较的东西，比如 node, 就会报错
                Python2 写法 import Queue
                qp = Queue.PriorityQueue
                只比第一个
                '''
        dummy = ListNode(0)
        cur = dummy
        while not qp.empty():
            _, i,cur.next = qp.get()
            cur = cur.next
            if cur.next:
                qp.put(cur.next.val,i, cur.next)
        return dummy.next

'''
循环写法
'''
class Solution(object):
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
            '''这个地方要注意要写'''
        def merget2List(l1,l2):
            if l1 == None:
                return l2
            if l2 == None:
                return l1
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
        k = len(lists)
        while k > 1:
            idx = 0
            for i in range(0,k,2):
                if i == k-1:
                    lists[idx] = lists[i] #单数链
                else:
                    lists[idx] = merget2List(lists[i], lists[i+1])
                idx += 1
            k = idx
        return lists[0]

'''
递归写法太简单就不写了。
'''


