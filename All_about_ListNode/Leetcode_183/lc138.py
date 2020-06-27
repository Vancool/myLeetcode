
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

'''
第二次做， 只想起来了哈希表方法
没想起来还有一个空间复杂度O(1)的拆分链表的方法
'''
class Solution(object):
    def copyRandomList(self, head):
        if not head: return head
        hashmap = {}
        cur = head
        hashmap[head] = Node(head.val)
        while cur:
            if cur.next:
                if cur.next not in hashmap:
                    hashmap[cur.next] = Node(cur.next.val)
                hashmap[cur].next = hashmap[cur.next]
            if cur.random:
                if cur.random not in hashmap:
                    hashmap[cur.random] = Node(cur.random.val)
                hashmap[cur].random = hashmap[cur.random]
            cur = cur.next
        return hashmap[head]

class Solution(object):
    def copyRandomList(self, head):
        if not head: return head
        cur = head
        while cur:
            tmp = cur.next
            cur.next = Node(cur.val)
            cur.next.next = tmp
            cur = tmp
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        next_head = head.next
        cur = head
        nextcur = next_head
        while cur:
            cur.next = nextcur.next
            cur = cur.next
            nextcur.next = cur.next if cur else None
            nextcur = nextcur.next
        return next_head



