class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        if len(postorder) == 0 or len(postorder) == 1:
            return True
        root = postorder[-1]
        m = len(postorder)
        i = m-2
        while i>= 0 and postorder[i] > root:
            i -= 1
        j = i
        while j >= 0:
            if postorder[j] > root:
                return False
            j -= 1
        return self.verifyPostorder(postorder[0:i+1]) and self.verifyPostorder(postorder[i+1: m-1])


a = Solution()
s = [1,3,2,6,5]
print(a.verifyPostorder(s))
print("Done")