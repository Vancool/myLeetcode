from collections import deque
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque()
        self.minstack = deque()


    def push(self, x):
        if len(self.stack) == 0 or (len(self.stack) > 0 and self.minstack[-1] >= x):
            self.minstack.append(x)
        self.stack.append(x)


    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        return self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        return self.minstack[-1]