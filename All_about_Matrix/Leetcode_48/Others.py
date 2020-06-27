'''
先找与转置矩阵的关系：
比如顺时针转90度其实就是转置矩阵，然后翻转一行
逆时针90°就是转置矩阵，翻转每列  180°就是沿着两条对角线各对称折一遍
'''
class Solution1:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n =len(matrix)
        # transpose matrix
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

                # reverse each row
        for i in range(n):
            matrix[i].reverse()
'''
关于算坐标赋值方法要注意：
1.如果不是递归操作而是循环操作注意找到到底要经历多少次循环
2.赋值方法
可以每次存一个4大小的数组记录旋转之前的数然后再来一次循环赋值[建议用这个，逆时针一个推另外三个好难算啊]
顺时针操作可以换成逆时针赋值
'''

class Solution2:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
class Solution3:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = [0] * 4
                row, col = i, j
                # store 4 elements in tmp
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    row, col = col, n - 1 - row
                # rotate 4 elements
                for k in range(4):
                    matrix[row][col] = tmp[(k - 1) % 4]
                    row, col = col, n - 1 - row