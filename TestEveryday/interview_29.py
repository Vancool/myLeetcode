class Solution(object):
    def spiralOrder(self, matrix):
        if len(matrix) == 0: return []
        m, n = len(matrix), len(matrix[0])
        res = []
        x, y = 0, 0
        margin = [0,0,0,0]
        while len(res) < m * n:
            while y < n - 1 - margin[0] and len(res) < m * n:
                res.append(matrix[x][y])
                y += 1
            margin[3] += 1
            while x < m - 1 - margin[1] and len(res) < m * n:
                res.append(matrix[x][y])
                x += 1
            margin[0] += 1
            while y > margin[2] and len(res) < m * n:
                res.append(matrix[x][y])
                y -= 1
            margin[1] += 1
            while x > margin[3] and len(res) < m * n:
                res.append(matrix[x][y])
                x -= 1
            margin[2] += 1
        return res
'''
没写出来
'''

a = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(a.spiralOrder(matrix))


