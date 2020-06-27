# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if l1.val == 0: return l2
        if l2.val == 0: return l1
        def process(node):
            if node == None: return 0
            node.val += process(node.next)
            res = node.val // 10
            node.val = int(node.val % 10)
            return res


        def addNum(longList, shortList, cutNode):
            dummy = ListNode(0)
            dummy.next = longList
            pre = dummy
            cur = pre.next
            while cutNode:
                cur = cur.next
                cutNode = cutNode.next
                pre = pre.next
            while cur:
                cur.val = cur.val + shortList.val
                cur = cur.next
                shortList = shortList.next
            process(dummy)
            return dummy if dummy.val == 1 else dummy.next
        cur1 = l1
        cur2 = l2
        while cur1 and cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        if cur1:
            #l1 比较长
            return addNum(l1, l2, cur1)
        else:
            return addNum(l2,l1, cur2)

'''
test case1: 
[1]
[9,9]
'''

'''
这题不是很难，主要是要注意进位导致了不能从中间
也可以先把l1 l2 倒转开始加，加完再把长链转换来
另一种解法：用双栈来解
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if l1.val == 0: return l2
        if l2.val == 0: return l1
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        cur = None
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            value = val1 + val2 + carry
            head = ListNode(int(value % 10))
            head.next = cur
            cur = head
            carry = value // 10
        return cur

'''
解法二.
也可以记录最近的一个没出现9的位置
然后只要出现10把这个位置+1 把这个位置之后的数变成0 然后找下一个不是9的位置
'''
'''
解法三. 我的解法写得还是太冗余了，其实可以直接找到cut算一个长度差，然后从尾巴处递归相加
传回去一个可能大于10的node, 然后在上一层解决进位问题
'''