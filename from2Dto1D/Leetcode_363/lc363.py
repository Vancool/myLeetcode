class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] <= k: res = max(res, matrix[i][j])
                if i ==0 and j == 0:
                     matrix[i][j] = matrix[i][j]
                elif i == 0:
                    matrix[i][j] = matrix[i][j] + matrix[i][j-1]
                elif j == 0:
                    matrix[i][j] = matrix[i][j] + matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i][j] + matrix[i-1][j] + matrix[i][j-1]-matrix[i-1][j-1]
                if matrix[i][j] <= k: res = max(res, matrix[i][j])
                for z in range(i-1, -1, -1):
                    if matrix[i][j] - matrix[z][j] <= k:
                        res = max(res,matrix[i][j] - matrix[z][j])
                for z in range(j-1,-1,-1):
                    if matrix[i][j] - matrix[i][z] <= k:
                        res = max(res,matrix[i][j] - matrix[i][z])
                if res == k: return k
        return res


'''
[[2,2,-1]]
0

res 是负数的情况没考虑

res是单个数的情况
'''
'''
这题真的好难， 我不会，注意要多看几次题解
https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/javacong-bao-li-kai-shi-you-hua-pei-tu-pei-zhu-shi/
https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/bao-li-onyou-hua-er-fen-er-fen-jian-zhi-by-lzh_yve/
'''

