from collections import deque
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.out = deque()
        self.enter = deque()
        self.enter_q = deque()


    def push(self, x):
        if len(self.out) > 0:
            self.enter.append(self.out.popleft())
        self.out.append(x)


    def pop(self):
        res = self.out.popleft()
        x = self.enter.popleft()
        while len(self.enter) > 0:
            self.out.append(x)
            x = self.enter.popleft()
        self.enter.append(x)
        self.enter, self.out = self.out, self.enter
        return res
    def top(self):
        return self.out[-1]


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.out) == 0 and len(self.enter) == 0
