from collections import deque
class MyStack(object):

    def __init__(self):
        self.q = deque()


    def push(self, x):
        self.q.append(x)
        while self.q[0] != x:
            self.q.append(self.q.popleft())


    def pop(self):
        if len(self.q) > 0:
            self.q.popleft()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.q) > 0:
            return self.q[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q) == 0

'''
我自己处理得还不够好
用一个队列处理的解法
'''


'''
用栈实现队列必须用两个栈，因为栈是从一头出来的
而用队列实现栈可以用一个队列， 因为队列可以一头出来放在另一头实现调转
'''


