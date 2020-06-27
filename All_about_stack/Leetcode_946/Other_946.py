from collections import deque
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if len(pushed) == 0:
            return len(popped) == 0
        if len(pushed)!= len(popped):
            return False
        stack = deque()
        i = 0
        for key in pushed:
            stack.append(key)
            while len(stack) > 0 and stack[-1] == popped[i]:
                i += 1
                stack.pop()
        return i == len(popped)