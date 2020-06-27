from collections import deque
class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        if len(postorder) == 0 or len(postorder) == 1:
            return True
        stack = deque()
        root = float('inf') #a dummy root to save a start(while)
        for i in range(len(postorder)-1,-1,-1):
            if postorder[i] > root:
                return False
            while len(stack) > 0 and postorder[i] < stack[-1]:
                # let's find key's root
                root = stack.pop()
            stack.append(postorder[i])
        return True

