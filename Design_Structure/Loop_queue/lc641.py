class Node(object):
    def __init__(self, val, pre=None, next=None):
        self.val = val
        self.pre = pre
        self.next = next

class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.total = k
        self.cur_num = k
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.pre = self.head
    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.cur_num > 0:
            new_node = Node(value, self.head, self.head.next)
            self.head.next.pre = new_node
            self.head.next = new_node
            self.cur_num -= 1
            return True
        return False

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.cur_num > 0:
            new_node = Node(value, self.tail.pre, self.tail)
            self.tail.pre.next = new_node
            self.tail.pre = new_node
            self.cur_num -= 1
            return True
        return False
    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.head.next = self.head.next.next
            # 我在此处少写了一步， 改 pre 指针
            self.head.next.pre = self.head
            self.cur_num += 1
            return True
        return False

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.tail.pre = self.tail.pre.pre
            # 同i样的这边也少写了一步， 改next指针
            self.tail.pre.next = self.tail
            self.cur_num += 1
            return True
        return False

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        res = -1
        if not self.isEmpty():
            res = self.head.next.val
        return res

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        res = -1
        if not self.isEmpty():
            res = self.tail.pre.val
        return res

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.cur_num == self.total

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.cur_num == 0

'''
我自己是用双端链表写的， 真是LRU后遗症

和 LRU 的区别： LRU是可以放进去的，所以只能用双端链表
               循环双端队列是不能放进去的，所以既可以用双端链表也可以用数组
               
数组的写法见 other
'''