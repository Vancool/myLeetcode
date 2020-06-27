class Node():
    def __init__(self, value=-1, key = -1):
        self.pre = None
        self.next = None
        self.key = key #这个key还是要的，因为删除尾节点的时候要知道删哈希表的哪个值
        self.val = value
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.hashMap = {}
        self.capacity = capacity
        self.cur_num = 0
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashMap:
            node = self.hashMap[key]
            self.insert2Head(node, False)
            return node.val
        else:
            return  -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hashMap:
            node = self.hashMap[key]
            node.val = value
            self.insert2Head(node, False)
        else:
            node = Node(value,key)
            self.insert2Head(node, True)
            self.hashMap[key] = node
            if self.cur_num < self.capacity:
                self.cur_num += 1
            else:
                tailNode = self.removeTail()
                del self.hashMap[tailNode.key]
    def removeTail(self):
        node = self.tail.pre
        node.pre.next = self.tail
        self.tail.pre = node.pre
        return node

    def insert2Head(self, node, is_new_node):
        if is_new_node:
            node.pre = self.head
            node.next = self.head.next

            self.head.next.pre = node
            self.head.next = node
        else:
            node.pre.next = node.next
            node.next.pre = node.pre

            node.pre = self.head
            node.next = self.head.next
            self.head.next.pre = node
            self.head.next = node

a = LRUCache(3)
a.put(1,1)
a.put(2,2)
a.put(3,3)
a.put(4,4)
a.get(4)
a.get(3)
a.get(2)
a.get(1)
a.put(5,5)
a.get(1)
a.get(2)
a.get(3)
a.get(4)
a.get(5)