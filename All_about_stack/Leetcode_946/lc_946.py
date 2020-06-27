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
        m = len(pushed)
        stack = deque()
        j = 0
        for i in range(m):
            while len(stack) and stack[-1] == popped[j]:
                j += 1
                stack.pop()
            if pushed[i] == popped[j]:
                j += 1
            else:
                stack.append(pushed[i])
        while j < m:
            if stack.pop()!= popped[j]:
                return False
            else:
                j += 1
        return True

a = Solution()
pushed = [3,2,1,0]
popped = [1,2,3,0]
print(a.validateStackSequences(pushed, popped))
print("Done")