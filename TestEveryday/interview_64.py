class Solution(object):
    def sumNums(self, n):

        return (n-1) & n * self.sumNums(n-1)