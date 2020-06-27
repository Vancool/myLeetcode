from collections import deque
class LRUCache(object):
    def __init__(self, capacity):
        self.max_num = capacity
        self.cur_num = 0
        self.stack = deque()
        self.dic = {}

    def get(self, key):
        if key in self.dic:
            if self.cur_num > 1:
                self.stack.appendleft(key)
                while self.stack[-1] == key or not self.stack[-1] in self.dic:
                    self.stack.pop()
            return self.dic[key]
        else:
            return -1
    def put(self, key, value):
        if key in self.dic:
            self.dic[key] = value
            if self.cur_num > 1:
                self.stack.appendleft(key)
                while self.stack[-1] == key or not self.stack[-1] in self.dic:
                    self.stack.pop()
        else:
            if self.cur_num == self.max_num:
                tmp = self.stack.pop()
                del self.dic[tmp]
                self.dic[key] = value
                self.stack.appendleft(key)
                while  not self.stack[-1] in self.dic:
                    self.stack.pop()
            else:
                self.cur_num += 1
                self.stack.appendleft(key)
                self.dic[key] = value
'''
test case
1.
["LRUCache","put","put","put","put","get","get"]
[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
a = LRUCache(2)
a.put(2,1)
a.put(1,1)
a.put(2,3)
a.put(4,1)
a.get(1)
a.get(2)
2.
["LRUCache","put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
[[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]

我写的是错的，没写出来
8个月前第一次写居然是用数组来写的，我都惊了
真不愧是我
正常来说是用双端链表写的
'''


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}  # dic include key-value
        self.stack = []  # save the order of key
        self.maxLength = capacity
        self.curLength = 0
        self.frequency = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if (len(self.dic) == 0 or not (self.dic.has_key(key))):
            return -1
        else:
            curIndex = self.stack.index(key)
            self.stack.insert(0, key)
            self.frequency[key] += 1
            return self.dic[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if (self.dic.has_key(key)):
            self.dic[key] = value
            curIndex = self.stack.index(key)
            self.stack.insert(0, key)
            self.frequency[key] += 1
        elif (self.curLength < self.maxLength):
            self.curLength = self.curLength + 1
            self.stack.insert(0, key)
            if (self.frequency.has_key(key)):
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            self.dic[key] = value
        elif (self.curLength == self.maxLength):
            outKey = self.stack.pop()
            while (self.frequency[outKey] > 1):
                self.frequency[outKey] -= 1
                outKey = self.stack.pop()
            self.frequency[outKey] -= 1
            del self.dic[outKey]
            self.stack.insert(0, key)
            if (self.frequency.has_key(key)):
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1

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