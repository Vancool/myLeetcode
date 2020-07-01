class MyCircularDeque(object):
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.capacity = k
        self.queue = [0] * k
        self.front = 0
        self.tail = 0
        self.size = 0

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.size += 1
            self.queue[self.front] = value
            self.front = int((self.front - 1 + self.capacity) % self.capacity)
            return True
        return False
    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.size += 1
            self.tail = int((self.tail + 1) % self.capacity)
            self.queue[self.tail] = value
            return True
        return False

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.front = int((self.front+1) % self.capacity)
            self.size -= 1
            return True
        return False
    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.size -= 1
            self.tail = int((self.tail-1+self.capacity) % self.capacity)
            return True
        return False
    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[int((self.front+1) % self.capacity)]
        return -1

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[int(self.tail % self.capacity)]
        return -1
    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.size == 0
    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.size ==  self.capacity