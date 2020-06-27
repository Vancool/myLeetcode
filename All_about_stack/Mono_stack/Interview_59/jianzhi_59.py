from collections import deque
class MaxQueue(object):

    def __init__(self):
        self.stack = deque()
        self.max_stack = deque()

    def max_value(self):
        """
        :rtype: int
        """
        return -1 if len(self.stack) == 0 else self.max_stack[0]
    '''
    注意题目只需要保持平均复杂度为O(1),而不是最大复杂度，因此维护一个递减栈是可以的
    因为 平均复杂度为 (O(1)*(n-1) + O(n-1)) / n = O(1)
    '''
    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        # max_stack 保持着一个递减序列
        while len(self.max_stack) > 0 and self.max_stack[-1] < value:
            self.max_stack.pop()
        self.max_stack.append(value)
        self.stack.append(value)
    def pop_front(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return -1
        if self.max_stack[0] == self.stack[0]:
            self.max_stack.popleft()
        return self.stack.popleft()