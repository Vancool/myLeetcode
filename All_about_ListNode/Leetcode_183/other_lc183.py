# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
'''
完全没看懂题目，看懂了发现原来是深拷贝（但是我也不知道深拷贝是什么
然后这题有两种解法
hash map 或者原地复制
如果不用hash map 每次查找的时候总要从头找一遍，很麻烦O(n^2)

'''
class Solution1(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = Node(cur.val, tmp, None)
            cur = tmp
        cur = head
        while cur:
            rNode = cur.random
            cur = cur.next
            if rNode == None:
                cur.random = None
            else:
                cur.random = rNode.next
            cur = cur.next
        copyHead = head.next
        cur = head
        copyCur = copyHead
        while cur:
            cur.next = copyCur.next
            copyCur.next = cur.next.next if cur.next else None
            cur = cur.next
            copyCur = copyCur.next
        return copyHead

'''
用哈希表的做法
和上面的做法的区别是需要用O(n)的哈希表来存储已经生成的节点
'''
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        hashset = {}
        cur = head
        while cur:
            hashset[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        while cur:
            hashset[cur].next = hashset[cur.next] if cur.next else None
            if cur.random:
                hashset[cur].random = hashset[cur.random]
            cur = cur.next
        return hashset[head]


