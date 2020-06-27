class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.stack_tmp = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        while self.stack:
            self.stack_tmp.append(self.stack.pop())
        self.stack.append(x)
        while self.stack_tmp:
            self.stack.append(self.stack_tmp.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stack:
            return self.stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack
'''
我这种实现还不太好，如果考虑平均每个入栈时间复杂度会达到 O(n)
但是实际上这个是可以达到 O(1)的平均时间复杂度的.
'''


class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.top = 0

    def push(self, x):
        if not self.stack1 and not self.stack2:
            self.top = x
        self.stack1.append(x)

    def pop(self):
        if self.stack2:
            res = self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            if self.stack2:
                res = self.stack2.pop()
        if self.stack2:
            self.top = self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            if self.stack2:
                self.top = self.stack2[-1]
        return res


    def peek(self):
        if self.stack1 or self.stack2:
            return self.top

    def empty(self):
        return not self.stack1 and not self.stack2

'''
自己写的时候有个corner case 没考虑到
["MyQueue","push","push","pop","push","push","pop","peek"]
[[],[1],[2],[],[3],[4],[],[]]
就是 stack2 之前有元素而弹出后没有元素的情况，这个时候也要从stack1导元素到stack2

我自己的写法不太好， 下面是比较好的写法
'''

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.popstack = []
        self.pushstack = []

    def shift(self):
        if not self.popstack:
            while self.pushstack:
                self.popstack.append(self.pushstack.pop())
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.pushstack.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.shift()
        if self.popstack:
            return self.popstack.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.shift()
        if self.popstack:
            return self.popstack[-1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.popstack and not self.pushstack

