class Node(object):
    def __init__(self, key, val):
        self.val = val
        self.pre = None
        self.next = None
        self.key = key
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.hashmap = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        res = -1
        if key in self.hashmap:
            node = self.hashmap[key]
            node.pre.next = node.next
            node.next.pre = node.pre
            node.next = self.head.next
            self.head.next.pre = node
            node.pre = self.head
            self.head.next = node
            res = node.val
        return res


    def put(self, key, value):
        if key in self.hashmap:
            self.get(key)
            self.head.next.val = value
        else:
            if self.capacity == 0:
                d_node = self.tail.pre
                if d_node.pre == None: return
                del self.hashmap[d_node.key]
                d_node.pre.next = d_node.next
                d_node.next.pre = d_node.pre
            else:
                self.capacity -= 1
            node = Node(key, value)
            self.hashmap[key] = node
            node.next = self.head.next
            self.head.next.pre = node
            node.pre = self.head
            self.head.next = node
'''
第三次写LRU
忘记区分 key 和 value
'''
