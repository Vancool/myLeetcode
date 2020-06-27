class Node:
    def __init__(self, value, pre=None, next=None):
        self.value = value
        self.pre = pre
        self.next = next
        self.key = set()
class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_value = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.tail.pre = self.head
        self.head.next = self.tail
        self.value_key = {}

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        if key not in self.key_value:
            self.key_value[key] = 1
            if 1 not in self.value_key:
                tmp = self.head.next
                cur = Node(1, self.head, tmp)
                tmp.pre = cur
                self.head.next = cur
                self.value_key[1] = cur
            self.value_key[1].key.add(key)
        else:
            v = self.key_value[key]
            self.value_key[v].key.remove(key)
            if len(self.value_key[v].key) == 0:
                self.value_key[v].pre.next = self.value_key[v].next
                self.value_key[v].next.pre = self.value_key[v].pre
            if v + 1 not in self.value_key:
                tmp = self.value_key[v].next
                pre = self.value_key[v] if len(self.value_key[v].key) > 0 else self.value_key[v].pre
                cur = Node(v + 1, pre, tmp)
                pre.next = cur
                tmp.pre = cur
            if len(self.value_key[v].key) <= 0:
                self.value_key.pop(v)
            self.value_key[v + 1] = cur
            self.value_key[v + 1].key.add(key)
            self.key_value[key] = v + 1
        print("inc ", key)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        if key in self.key_value:
            value = self.key_value[key]
            self.key_value[key] -= 1
            self.value_key[value].key.remove(key)
            if len(self.value_key[value].key) == 0:
                self.value_key[value].pre.next = self.value_key[value].next
                self.value_key[value].next.pre = self.value_key[value].pre
            if self.key_value[key] == 0:
                self.key_value.pop(key)
            else:
                if value-1 not in self.value_key:
                    pre = self.value_key[value] if len(self.value_key[value].key) > 0 else self.value_key[value].pre
                    tmp = self.value_key[value].next
                    cur = Node(value-1, pre, tmp)
                    pre.next = cur
                    tmp.pre = cur
                    self.value_key[value-1] = cur
                self.value_key[value-1].key.add(key)
            if len(self.value_key[value].key) == 0:
                self.value_key.pop(value)
        print("delete ", key)
    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.head.next != self.tail:
            key = self.tail.pre.key.pop()
            self.tail.pre.key.add(key)
            return key
        return ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: strh
        """
        if self.head.next != self.tail:
            key = self.head.next.key.pop()
            self.head.next.key.add(key)
            return key
        return ""
#
# ["AllOne","inc","inc","inc","inc","getMaxKey","inc","inc","inc","dec","inc","inc","inc","getMaxKey"]
# [[],["hello"],["goodbye"],["hello"],["hello"],[],["leet"],["code"],["leet"],["hello"],["leet"],["code"],["code"],[]]

# ["AllOne","inc","inc","inc","inc","inc","inc","dec", "dec","getMinKey","dec","getMaxKey","getMinKey"]
# [[],["a"],["b"],["b"],["c"],["c"],["c"],["b"],["b"],[],["a"],[],[]]
#
# ["AllOne","inc","inc","inc","dec","inc","inc","getMaxKey","dec","dec","dec","getMaxKey"]
# [[],["hello"],["world"],["hello"],["world"],["hello"],["leet"],[],["hello"],["hello"],["hello"],[]]
a = AllOne()
a.inc("hello")
a.inc("world")
a.inc("hello")
a.dec("world")
a.inc("world")
a.inc("leet")
print(a.getMaxKey())
a.dec("hello")
a.dec("hello")
a.dec("hello")

'''
这题我思路是对的，但是就是没写出来，写得太乱了， 要分块
二刷的时候需要再写一遍
'''


print(a.getMaxKey())
#print(a.getMinKey())


