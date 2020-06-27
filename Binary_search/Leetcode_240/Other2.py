'''

从另外一个口开始搜索，将矩阵转化为一个二叉搜索问题
如果大于当前值向左走(往左减小)， 小于当前值向下走(往下增大)，直到走出矩阵为止
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == None or len(matrix) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        x = 0
        y = n-1
        while x<m and y >= 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False